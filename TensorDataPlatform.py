import altair as alt
import math
import pandas as pd
import streamlit as st
import requests


st.set_page_config(layout="wide")  # this needs to be the first Streamlit command

st.title("Tensor Data Platform")
#LAT
#huobi
r=requests.get("https://api.huobi.pro/market/history/kline?period=1day&size=100&symbol=latusdt")
a=pd.DataFrame(pd.read_json(r.text)["data"].tolist())
huobi=pd.DataFrame({"t":a["id"],"symbol":"huobi","Volume":a["amount"]}).iloc[::-1]
huobi["t"]=pd.to_datetime(huobi["t"],unit="s")
#okex
r=requests.get("https://www.okex.com/api/v5/market/history-candles?instId=LAT-USDT&bar=1D")
b=pd.DataFrame(pd.read_json(r.text)["data"].tolist(),columns=["id","open","high","low","close","vol","volCcy"])
okex=pd.DataFrame({"t":b["id"],"symbol":"okex","Volume":b["vol"]}).iloc[::-1]
okex["t"]=pd.to_datetime(okex["t"],unit="ms")
#concat
Volume=pd.concat([huobi,okex])
#concat
c=pd.concat([huobi,okex])

st.header("huobi")
st.write(huobi)

st.header("okex")
st.write(okex)

st.header("c")
st.write(c)

