import altair as alt
import math
import pandas as pd
import streamlit as st
import requests


st.set_page_config(layout="wide")  # this needs to be the first Streamlit command

st.title("Tensor Data Platform")
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
#combine
Volume=pd.concat([huobi,okex])


st.header("huobi")
st.write(huobi)

st.header("okex")
st.write(okex)

st.header("Volume")
st.write(Volume)

