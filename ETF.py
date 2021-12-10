import requests
import pandas as pd
import numpy as np
import time
import altair as alt
import streamlit as st


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
  a=alt.Chart(dfeth.tail(30)).mark_bar().encode(
      x=alt.X("yearmonthdate(statisDate):T",axis=alt.Axis(title=None)),
      y=alt.Y("value:Q",axis=alt.Axis(title="ETH持仓变化")),
      color="indicatorName:N"   
  ).properties(
      width=800,
      height=350
  ).interactive()
  b=alt.Chart(dfbtc.tail(30)).mark_bar().encode(
      x=alt.X("yearmonthdate(statisDate):T",axis=alt.Axis(title=None)),
      y=alt.Y("value:Q",axis=alt.Axis(title="BTC持仓变化")),
      color="indicatorName:N"   
  ).properties(
      width=800,
      height=350
  ).interactive()
  return a,b

def set_ETF():
  t1, t2= st.columns(2)
  with t1:
    st.header("ETH 持仓变化")
    st.write(getETF()[0])
  with t2:
    st.header("BTC 持仓变化")
    st.write(getETF()[1])
