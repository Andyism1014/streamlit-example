import altair as alt
import math
import pandas as pd
import requests
import streamlit as st


def getbithumb(x):
  name=x.upper()+"_KRW"+"/24h"
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


def gethuobi(x):
  name=x.lower()+"usdt"
  r=requests.get("https://api.huobi.pro/market/history/kline",params={"size":1000,"symbol":name,"period":"1day"})
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


def getok(x):
  name=x.upper()+"-USDT"
  r=requests.get("https://www.okex.com/api/v5/market/history-candles",params={"instId":name,"bar":"1D"})
  if r.json()["msg"]=="Token does not exist.":
    return "error"
  else:
    r=requests.get("https://www.okex.com/api/v5/market/history-candles",params={"instId":name,"bar":"1D"})
    a=pd.DataFrame(r.json()["data"])
    while(len(r.json()["data"])==100):
      nt=str(a[0].iloc[-1])
      r=requests.get("https://www.okex.com/api/v5/market/history-candles",params={"instId":name,"bar":"1D","after":nt})
      b=pd.DataFrame(r.json()["data"])
      a=pd.concat([a,b],ignore_index=True)
    else:
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


def getbinance(x):
  name=x.upper()+"USDT"
  r=requests.get("https://api.binance.com/api/v3/klines",params={"limit":1000,"interval":"1d","symbol":name})
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


def getinfor(x):
  b=[]
  c=[]
  a=[getbinance(x),getok(x),getbithumb(x),gethuobi(x)]
  for i in a:
    if isinstance(i, pd.DataFrame) is True:
      b.append(i)
  for i in b:
    c.append(len(i))
  m=c.index(max(c))
  return [b,b[m]]

@st.experimental_memo
def PaintVP(x):
  V=pd.concat(x[0])
  a=alt.Chart(x[1]).mark_line().encode(
      x=alt.X("yearmonthdate(t):T",axis=alt.Axis(title=None)),
      y='Price:Q')
  b=alt.Chart(V).mark_area(opacity=0.6).encode(
      x=alt.X("yearmonthdate(t):T",axis=alt.Axis(title=None)),
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
      x=alt.X("yearmonthdate(t):T",axis=alt.Axis(title=None)),
      y=alt.Y("Volume:Q",axis=alt.Axis(format="s",title="14 days Moving Average")),
      color="symbol:N")
  res2=alt.layer(a,b).resolve_scale(
      y = 'independent').properties(
      width=800,
      height=350
  ).interactive(bind_y=False)
  return [res1,res2]


def set_Portfolio2():
    st.header("LAT Consolidated Volume")
    st.write(PaintVP(getinfor("lat"))[0])
    st.write(PaintVP(getinfor("lat"))[1])
    st.header("CKB Consolidated Volume")
    st.write(PaintVP(getinfor("CKB"))[0])
    st.write(PaintVP(getinfor("CKB"))[1])
    st.header("KLAY Consolidated Volume")
    st.write(PaintVP(getinfor("KLAY"))[0])
    st.write(PaintVP(getinfor("KLAY"))[1])