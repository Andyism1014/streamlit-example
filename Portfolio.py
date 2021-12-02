import altair as alt
import math
import pandas as pd
import requests
import streamlit as st



def getLAT():
  #LAT
  r=requests.get("https://api.huobi.pro/market/history/kline?period=1day&size=100&symbol=latusdt")
  a=pd.DataFrame(pd.read_json(r.text)["data"].tolist())
  huobi=pd.DataFrame({"t":a["id"],"symbol":"huobi","Volume":a["amount"]}).iloc[::-1]
  huobi["t"]=pd.to_datetime(huobi["t"],unit="s")
  #okex
  r=requests.get("https://www.okex.com/api/v5/market/history-candles?instId=LAT-USDT&bar=1D")
  a=pd.DataFrame(pd.read_json(r.text)["data"].tolist(),columns=["id","open","high","low","close","vol","volCcy"])
  a["vol"]=pd.to_numeric(a["vol"])
  okex=pd.DataFrame({"t":a["id"],"symbol":"okex","Volume":a["vol"]}).iloc[::-1]
  okex["t"]=pd.to_datetime(okex["t"],unit="ms")
  ##concat
  Volume=pd.concat([huobi,okex],ignore_index=True)
  #MovingAverage
  huobi["Volume"]=huobi["Volume"].rolling(14).mean()
  okex["Volume"]=okex["Volume"].rolling(14).mean()
  MAVLAT=pd.concat([huobi,okex])
  r=requests.get("https://api.huobi.pro/market/history/kline?period=1day&size=100&symbol=latusdt")
  a=pd.DataFrame(pd.read_json(r.text)["data"].tolist())
  Price=pd.DataFrame({"t":pd.to_datetime(a["id"],unit="s"),"Price":(a["high"]+a["low"])/2})
  a=alt.Chart(Price).mark_line().encode(
      x=alt.X("yearmonthdate(t):T",axis=alt.Axis(title=None)),
      y='Price:Q')
  b=alt.Chart(Volume).mark_area(opacity=0.6).encode(
      x=alt.X("yearmonthdate(t):T",axis=alt.Axis(title=None)),
      y=alt.Y("Volume:Q",axis=alt.Axis(format="s")),
      color="symbol:N")
  res1=alt.layer(a,b).resolve_scale(
      y = 'independent').properties(
      width=800,
      height=350
  ).interactive(bind_y=False)
  c=alt.Chart(MAVLAT).mark_area(opacity=0.6).encode(
      x=alt.X("yearmonthdate(t):T",axis=alt.Axis(title=None)),
      y=alt.Y("Volume:Q",axis=alt.Axis(format="s",title="14days Moving Average")),
      color="symbol:N"  
  )
  res2=alt.layer(a,c).resolve_scale(
      y = 'independent').properties(
      width=800,
      height=350
  ).interactive(bind_y=False)
  return [res1,res2]

def getCKB(): 
  #CKB
  #binance
  r=requests.get("https://api.binance.com/api/v3/klines?symbol=CKBUSDT&interval=1d&limit=1000")
  a=pd.read_json(r.text)
  a[5]=pd.to_numeric(a[5])
  binance=pd.DataFrame({"t":pd.to_datetime(a[0],unit="ms"),"symbol":"binance","Volume":a[5]})
  #bithumb vol in currency
  r=requests.get("https://api.bithumb.com/public/candlestick/CKB_KRW/24h")
  a=pd.DataFrame(pd.read_json(r.text)["data"].tolist())
  a[5]=pd.to_numeric(a[5])
  bithumb=pd.DataFrame({"t":pd.to_datetime(a[0],unit="ms"),"symbol":"bithumb","Volume":a[5]})
  #huobi
  r=requests.get("https://api.huobi.pro/market/history/kline?period=1day&size=1000&symbol=ckbusdt")
  a=pd.DataFrame(pd.read_json(r.text)["data"].tolist())
  a["amount"]=pd.to_numeric(a["amount"])
  huobi=pd.DataFrame({"t":pd.to_datetime(a["id"],unit="s"),"symbol":"huobi","Volume":a["amount"]}).iloc[::-1]
  #concat
  Volume=pd.concat([huobi,bithumb,binance])
  #price
  r=requests.get("https://api.huobi.pro/market/history/kline?period=1day&size=1000&symbol=ckbusdt")
  a=pd.DataFrame(pd.read_json(r.text)["data"].tolist())
  Price=pd.DataFrame({"t":pd.to_datetime(a["id"],unit="s"),"Price":(a["high"]+a["low"])/2})
  #MovingAverage
  binance["Volume"]=binance["Volume"].rolling(14).mean()
  bithumb["Volume"]=bithumb["Volume"].rolling(14).mean()
  huobi["Volume"]=huobi["Volume"].rolling(14).mean()
  MAV=pd.concat([binance,bithumb,huobi])
  #picture
  a=alt.Chart(Price).mark_line().encode(
      x=alt.X("yearmonthdate(t):T",axis=alt.Axis(title=None)),
      y='Price:Q'
  )
  b=alt.Chart(Volume).mark_area(opacity=0.6).encode(
      x=alt.X("yearmonthdate(t):T",axis=alt.Axis(title=None)),
      y=alt.Y("Volume:Q",axis=alt.Axis(format="s")),
      color="symbol:N"
      
  )

  res1=alt.layer(a,b).resolve_scale(
      y = 'independent').properties(
      width=800,
      height=350
  ).interactive(bind_y=False)


  c=alt.Chart(MAV).mark_area(opacity=0.6).encode(
      x=alt.X("yearmonthdate(t):T",axis=alt.Axis(title=None)),
      y=alt.Y("Volume:Q",axis=alt.Axis(format="s",title="14days Moving Average")),
      color="symbol:N"
      
  )

  res2=alt.layer(a,c).resolve_scale(
      y = 'independent').properties(
      width=800,
      height=300
  ).interactive(bind_y=False)
  return res1,res2

def set_Portfolio():
    st.header("LATConsolidated Volume")
    st.write(getLAT()[0])
    st.write(getLAT()[1])
    st.header("CKBConsolidated Volume")
    st.write(getCKB()[0])
    st.write(getCKB()[1])