import altair as alt
import math
import pandas as pd
import streamlit as st
import requests


st.set_page_config(layout="wide")  # this needs to be the first Streamlit command

st.title("Tensor Data Platform")

col1, col2, col3 = st.columns(3)
left,right=st.columns(2)
  
# LAT
#huobi
r=requests.get("https://api.huobi.pro/market/history/kline?period=1day&size=100&symbol=latusdt")
a=pd.DataFrame(pd.read_json(r.text)["data"].tolist())
huobi=pd.DataFrame({"t":a["id"],"symbol":"huobi","Volume":a["amount"]}).iloc[::-1]
huobi["t"]=pd.to_datetime(huobi["t"],unit="s")

#okex
r=requests.get("https://www.okex.com/api/v5/market/history-candles?instId=LAT-USDT&bar=1D")
a=pd.DataFrame(pd.read_json(r.text)["data"].tolist(),columns=["id","open","high","low","close","vol","volCcy"])
okex=pd.DataFrame({"t":a["id"],"symbol":"okex","Volume":a["vol"]}).iloc[::-1]
okex["t"]=pd.to_datetime(okex["t"],unit="ms")
#concat
Volume=pd.concat([huobi,okex])

#price
r=requests.get("https://api.huobi.pro/market/history/kline?period=1day&size=100&symbol=latusdt")
a=pd.DataFrame(pd.read_json(r.text)["data"].tolist())
Price=pd.DataFrame({"t":pd.to_datetime(a["id"],unit="s"),"Price":(a["high"]+a["low"])/2})

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

#layout
with left:
  st.header("Huobi")
  st.write(res1)


