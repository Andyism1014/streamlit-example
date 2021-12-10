import requests
import pandas as pd
import numpy as np
import time
import altair as alt
import streamlit as st
from datetime import date
from datetime import timedelta

def get_g(x,y,z,g):
  API_KEY = '1zza0Y66PQqo0LoeJXRooWgj41F'
  res = requests.get("https://api.glassnode.com"+y,
      params={'a':x,"timestamp_format":"humanized",'api_key':API_KEY,"i":z})
  # convert to pandas dataframe
  df = pd.read_json(res.text)
  return df.tail(g)

def get_g_ex(x,y,e,g):
  API_KEY = '1zza0Y66PQqo0LoeJXRooWgj41F'
  res = requests.get("https://api.glassnode.com"+y,
      params={'a':x,"timestamp_format":"humanized",'api_key':API_KEY,"e":e})
  # convert to pandas dataframe
  df = pd.read_json(res.text)
  return df.tail(g)


@st.experimental_memo(ttl=60*60*24)
def get_netdata(x):
  x=x.upper()
  if x=="BTC":
    list= ['binance','coinbase','huobi','kraken','okex',"kucoin","bitfinex","bithumb","gate.io","bitstamp"]
  else:
    list= ['binance','huobi','kraken','okex',"kucoin","bitfinex","bithumb","gate.io"]
  for i in list:
    if list.index(i)==0:
      df=get_g_ex(x,"/v1/metrics/distribution/exchange_net_position_change",i,30)
      df["symbol"]=i.capitalize() 
    else:
      b=get_g_ex(x,"/v1/metrics/distribution/exchange_net_position_change",i,30)
      b["symbol"]=i.capitalize() 
      df=pd.concat([df,b],ignore_index=True)
  return df

@st.experimental_memo
def plot_netdata(df):
  res=alt.Chart(df).mark_bar().encode(
      x=alt.X("t:T",axis=alt.Axis(title="Time")),
      y=alt.Y('v:Q',axis=alt.Axis(format="s",title="Net Position Change")),
      color="symbol:N",
      tooltip=[alt.Tooltip('t:T', title='Time'),alt.Tooltip('v:Q', title='Net Position Change',format="s"),alt.Tooltip('symbol:N', title='Net Position Exchange')]).properties(
        width=700,
        height=350
    ).interactive(bind_y=False)
  return res


@st.experimental_memo(ttl=60*60*24)
def getETF():
  #get update time:
  r=requests.get("https://www.oklink.com/api/oklink/v1/eth/datamaster/market/201",headers={"x-apiKey":"962feef7-6c1d-4c49-9ca2-dfc9a9d438bc"},params={
    "startTime":1619280000000,
    "endTime":1637542800000})
  df=pd.read_json(r.text)
  t=df["data"]["updateTime"]
  #get data:
  ethurl=["https://www.oklink.com/api/oklink/v1/eth/datamaster/market/201",
          "https://www.oklink.com/api/oklink/v1/eth/datamaster/market/203",
          "https://www.oklink.com/api/oklink/v1/eth/datamaster/market/205",
          "https://www.oklink.com/api/oklink/v1/eth/datamaster/market/103",
          "https://www.oklink.com/api/oklink/v1/eth/datamaster/market/101"]
  btcurl=["https://www.oklink.com/api/oklink/v1/btc/datamaster/market/207",
          "https://www.oklink.com/api/oklink/v1/btc/datamaster/market/209",
          "https://www.oklink.com/api/oklink/v1/btc/datamaster/market/211",
          "https://www.oklink.com/api/oklink/v1/btc/datamaster/market/25",
          "https://www.oklink.com/api/oklink/v1/btc/datamaster/market/23"]
  for i in ethurl:
    if ethurl.index(i)==0:
      r=requests.get(i,headers={"x-apiKey":"962feef7-6c1d-4c49-9ca2-dfc9a9d438bc"},params={
        "startTime":1619280000000,
        "endTime":t})
      df=pd.read_json(r.text)
      b=pd.DataFrame(df["data"]["content"])
      b["indicatorName"]=df["data"]["indicatorName"]
      b["statisDate"]=pd.to_datetime(b["statisDate"],unit="ms")
    else:
      r=requests.get(i,headers={"x-apiKey":"962feef7-6c1d-4c49-9ca2-dfc9a9d438bc"},params={
        "startTime":1619280000000,
        "endTime":t})
      df=pd.read_json(r.text)
      c=pd.DataFrame(df["data"]["content"])
      c["indicatorName"]=df["data"]["indicatorName"]
      c["statisDate"]=pd.to_datetime(b["statisDate"],unit="ms")
      b=pd.concat([b,c],ignore_index=True)
  dfeth=b
  for i in btcurl:
    if btcurl.index(i)==0:
      r=requests.get(i,headers={"x-apiKey":"962feef7-6c1d-4c49-9ca2-dfc9a9d438bc"},params={
        "startTime":1619280000000,
        "endTime":t})
      df=pd.read_json(r.text)
      b=pd.DataFrame(df["data"]["content"])
      b["indicatorName"]=df["data"]["indicatorName"]
      b["statisDate"]=pd.to_datetime(b["statisDate"],unit="ms")
    else:
      r=requests.get(i,headers={"x-apiKey":"962feef7-6c1d-4c49-9ca2-dfc9a9d438bc"},params={
        "startTime":1619280000000,
        "endTime":t})
      df=pd.read_json(r.text)
      c=pd.DataFrame(df["data"]["content"])
      c["indicatorName"]=df["data"]["indicatorName"]
      c["statisDate"]=pd.to_datetime(b["statisDate"],unit="ms")
      b=pd.concat([b,c],ignore_index=True)
  dfbtc=b
  today = date.today()
  yesterday = today - timedelta(days = 60)
  domain=[today.strftime('%Y-%m-%d'),yesterday.strftime('%Y-%m-%d')]
  a=alt.Chart(dfeth).mark_bar().encode(
      x=alt.X("yearmonthdate(statisDate):T",axis=alt.Axis(title=None),scale=alt.Scale(domain=domain)),
      y=alt.Y("value:Q",axis=alt.Axis(title="ETH持仓变化")),
      color="indicatorName:N"   
  ).properties(
      width=800,
      height=350
  ).interactive()
  b=alt.Chart(dfbtc).mark_bar().encode(
      x=alt.X("yearmonthdate(statisDate):T",axis=alt.Axis(title=None),scale=alt.Scale(domain=domain)),
      y=alt.Y("value:Q",axis=alt.Axis(title="BTC持仓变化")),
      color="indicatorName:N"   
  ).properties(
      width=800,
      height=350
  ).interactive()
  return a,b

def set_ETF():
  st.title("On-Chain Data")
  t1, t2= st.columns(2)
  with t2:
    st.header("ETH Institutions")
    st.write(getETF()[0])
    st.write(plot_netdata(get_netdata("ETF")))
  with t1:
    st.header("BTC Institutions")
    st.write(getETF()[1])
    st.write(plot_netdata(get_netdata("BTC")))

