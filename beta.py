import altair as alt
import math
import pandas as pd
import requests
import streamlit as st
import time
import streamlit.components.v1 as components

@st.experimental_memo(ttl=60)
def getbithumb(x,y):
  if y=="d":
    period="24h"
  elif y=="m":
    period="1m"
  name=x.upper()+"_KRW"+"/"+period
  r=requests.get("https://api.bithumb.com/public/candlestick/"+name)
  if r.json()["status"]!="0000":
    return "error"
  else:
    a=pd.DataFrame(r.json()["data"])
    a=a.tail(1000)
    a["t"]=pd.to_datetime(a[0],unit="ms")
    a[2]=pd.to_numeric(a[2])
    a[3]=pd.to_numeric(a[3])
    a[5]=pd.to_numeric(a[5])
    a["symbol"]="Bithumb"
    a["Volume"]=a[5]
    a["Price"]=(a[2]+a[3])/(2*1180.76)
    a=a[["t","symbol","Price","Volume"]]
    return a

@st.experimental_memo(ttl=60)
def gethuobi(x,y):
  if y=="d":
    period="1day"
  elif y=="m":
    period="1min"
  name=x.lower()+"usdt"
  r=requests.get("https://api.huobi.pro/market/history/kline",params={"size":1000,"symbol":name,"period":period})
  if r.json()["status"]=="error":
    return "error"
  else:
    a=pd.json_normalize(r.json()["data"])
    a["id"]=pd.to_datetime(a["id"],unit="s")
    a=a.sort_values(by="id",ignore_index=True)
    a["symbol"]="Huobi"
    a=a.rename(columns={"id":"t", "amount":"Volume"})
    a["Price"]=(a["low"]+a["high"])/2
    a=a[["t","symbol","Price","Volume"]]
    return a

@st.experimental_memo(ttl=60)
def getok(x,y):
  if y=="d":
    bar="1D"
  elif y=="m":
    bar="1m"
  name=x.upper()+"-USDT"
  r=requests.get("https://www.okex.com/api/v5/market/history-candles",params={"instId":name,"bar":bar})
  if r.json()["msg"]=="Token does not exist.":
    return "error"
  else:
    r=requests.get("https://www.okex.com/api/v5/market/history-candles",params={"instId":name,"bar":bar})
    a=pd.DataFrame(r.json()["data"])
    while(len(r.json()["data"])==100):
      nt=str(a[0].iloc[-1])
      r=requests.get("https://www.okex.com/api/v5/market/history-candles",params={"instId":name,"bar":bar,"after":nt})
      b=pd.DataFrame(r.json()["data"])
      a=pd.concat([a,b],ignore_index=True)
      if len(a)==1000:
        break
    a[0]=pd.to_datetime(a[0],unit="ms")
    a[2]=pd.to_numeric(a[2])
    a[3]=pd.to_numeric(a[3])
    a[5]=pd.to_numeric(a[5])
    a=a.sort_values(by=0,ignore_index=True)
    a["symbol"]="Okex"
    a["Price"]=(a[2]+a[3])/2
    a=a.rename(columns={0:"t", 5:"Volume"})
    a=a[["t","symbol","Price","Volume"]]
    return a

@st.experimental_memo(ttl=60)
def getbinance(x,y):
  if y=="d":
    bar="1d"
  elif y=="m":
    bar="1m"
  name=x.upper()+"USDT"
  r=requests.get("https://api.binance.com/api/v3/klines",params={"limit":1000,"interval":bar,"symbol":name})
  if len(r.json())<3:
    return "error"
  else:
    a=pd.read_json(r.text)
    a[0]=pd.to_datetime(a[0],unit="ms")
    a["symbol"]="Binance"
    a=a.rename(columns={0:"t", 5:"Volume"})
    a["Price"]=(a[2]+a[3])/2
    a=a[["t","symbol","Price","Volume"]]
    return a

@st.experimental_memo(ttl=60)
def getinfor(x,y):
  b=[]
  c=[]
  a=[getbinance(x,y),getok(x,y),getbithumb(x,y),gethuobi(x,y)]
  for i in a:
    if isinstance(i, pd.DataFrame) is True:
      b.append(i)
  for i in b:
    c.append(len(i))
  m=c.index(max(c))
  return [b,b[m],y]

@st.experimental_memo
def PaintVP(x):
  if x[2]=="m":
    per="t:T"
  if x[2]=="d":
    per="yearmonthdate(t):T"
  V=pd.concat(x[0])
  a=alt.Chart(x[1]).mark_line().encode(
      x=alt.X(per,axis=alt.Axis(title=None)),
      y=alt.Y('Price:Q',scale=alt.Scale(zero=False)),
      tooltip=['Price']
      )
  b=alt.Chart(V).mark_area(opacity=0.6).encode(
      x=alt.X(per,axis=alt.Axis(title=None)),
      y=alt.Y("Volume:Q",axis=alt.Axis(format="s")),
      color="symbol:N")
  res1=alt.layer(a,b).resolve_scale(
      y = 'independent').properties(
      width=800,
      height=350
  ).interactive(bind_y=False)
  for i in x[0]:
    i["Volume"]=i["Volume"].rolling(14).mean()
  V=pd.concat(x[0])
  b=alt.Chart(V).mark_area(opacity=0.6).encode(
      x=alt.X(per,axis=alt.Axis(title=None)),
      y=alt.Y("Volume:Q",axis=alt.Axis(format="s"),title="Volume Moving Average"),
      color="symbol:N")
  res2=alt.layer(a,b).resolve_scale(
      y = 'independent').properties(
      width=800,
      height=350
  ).interactive(bind_y=False)
  return [res1,res2]

@st.experimental_memo
def findcmcID(x):
  x.upper()
  r=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/map",headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '33ee501d-ff77-4c6a-9fdb-cec868e22981',
  },params={"symbol":x})
  return r.json()["data"][0]["id"] 

def set_one(x):
  x=x.upper()
  col1, col2= st.columns(2)
  with col1:
    st.header(x+" price information")
    a=findcmcID(x)
    components.html("""
    <script type="text/javascript" src="https://files.coinmarketcap.com/static/widget/currency.js">
    </script><div class="coinmarketcap-currency-widget" data-currencyid=%s data-base="USD" data-secondary="" 
    data-ticker="true" data-rank="false" data-marketcap="true" data-volume="true" data-statsticker="true" data-stats="USD">
    </div>
    """%(a),
    width=700)
  with col2:
    st.header(x+" Consolidated Volume")
    if st.button('days'):
      st.write(PaintVP(getinfor(x,"d"))[0])
      st.write(PaintVP(getinfor(x,"d"))[1])
    if st.button('1 min'):
      st.write(PaintVP(getinfor(x,"m"))[0])
      st.write(PaintVP(getinfor(x,"m"))[1])



def set_Portfolio():
  set_one("lat")
  set_one("ckb")


