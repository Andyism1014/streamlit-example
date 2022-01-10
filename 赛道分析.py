import plotly.graph_objects as go
import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as components
from st_aggrid import AgGrid,GridOptionsBuilder,GridUpdateMode, DataReturnMode, JsCode
from streamlit.proto.Button_pb2 import Button
from plotly.subplots import make_subplots
from datetime import datetime
import numpy as np




@st.experimental_memo(ttl=60*60*24)
def messariP(x):
  today=datetime.today().strftime('%Y-%m-%d')
  url="https://data.messari.io/api/v1/assets/%s/metrics/price/time-series"%(x)
  header={ "x-messari-api-key": "77fd912b-7c49-449f-a808-d3755b9bb69a"}
  r=requests.get(url,headers=header,params = {"start":"2021-01-01","end":today,"interval":"1d","columns":"close"})
  df=pd.DataFrame(r.json()["data"]["values"])
  return df

config = {'displaylogo': False, 'modeBarButtonsToRemove': ["zoomIn", "zoomOut", "autoScale","resetScale"],'modeBarButtonsToAdd':['drawline','drawopenpath', 'drawrect','eraseshape'],}

lay1=["SOL","BNB","ADA","MATIC","AVAX","LUNA","DOT","ALGO","TRX","FTM"]
def messari():
  fig=go.Figure()
  with st.expander("Edit"):
    slider=int(st.slider("Moving average",min_value=1,max_value=100,step=1,key=0))
    inwhat=st.selectbox("Alpha in",["ETH","BTC"])
  ethP=messariP(inwhat)
  for i in lay1:
    df=messariP(i)
    df[1]=df[1]/ethP[1]
    df[1]=df[1].pct_change()
    df[1]=df[1]+1
    df[1]=df[1].cumprod()
    df[0]=pd.to_datetime(df[0], unit="ms").dt.date
    fig.add_trace(go.Scatter(
        x=df[0],
        y=df[1].rolling(slider).mean(),
        name=i
      ))
  fig.update_layout(
    yaxis=dict(tickformat=".2%"),
    title_text="Layer 1 in "+inwhat,
    legend=dict(
    orientation="h",
    yanchor="top",
    y=-0.05,
    xanchor="left",
    x=0
   )
  )
  st.plotly_chart(fig, use_container_width=True,config=config)



messari()