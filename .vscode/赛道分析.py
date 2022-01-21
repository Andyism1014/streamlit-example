import plotly.graph_objects as go
import pandas as pd
import requests
import streamlit as st
from datetime import datetime
import json


@st.experimental_memo(ttl=60 * 60 * 24)
def messariP(x):
    today = datetime.today().strftime('%Y-%m-%d')
    url = "https://data.messari.io/api/v1/assets/%s/metrics/price/time-series" % x
    header = {"x-messari-api-key": "77fd912b-7c49-449f-a808-d3755b9bb69a"}
    r = requests.get(url, headers=header,
                     params={"start": "2021-01-01", "end": today, "interval": "1d", "columns": "close"})
    df = pd.DataFrame(r.json()["data"]["values"])
    return df


config = {'displaylogo': False, 'modeBarButtonsToRemove': ["zoomIn", "zoomOut", "autoScale", "resetScale"],
          'modeBarButtonsToAdd': ['drawline', 'drawopenpath', 'drawrect', 'eraseshape'], }

lay1 = ["SOL", "BNB", "ADA", "MATIC", "AVAX", "LUNA", "DOT", "ALGO", "TRX", "FTM"]


def messari():
    fig = go.Figure()
    with st.expander("Edit"):
        slider = int(st.slider("Moving average", min_value=1, max_value=100, step=1, key=0))
        inwhat = st.selectbox("Alpha in", ["ETH", "BTC"])
    ethp = messariP(inwhat)
    for i in lay1:
        df = messariP(i)
        df[1] = df[1] / ethp[1]
        df[1] = df[1].pct_change()
        df[1] = df[1] + 1
        df[1] = df[1].cumprod()
        df[0] = pd.to_datetime(df[0], unit="ms").dt.date
        fig.add_trace(go.Scatter(
            x=df[0],
            y=df[1].rolling(slider).mean(),
            name=i
        ))
    fig.update_layout(
        yaxis=dict(tickformat=".2%"),
        title_text="Layer 1 in " + inwhat,
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.05,
            xanchor="left",
            x=0
        )
    )
    st.plotly_chart(fig, use_container_width=True, config=config)


def get_json_data():
    a=[]
    for i in range(2):
        url = "https://data.messari.io/api/v2/assets?fields=symbol,metrics" 
        header = {"x-messari-api-key": "77fd912b-7c49-449f-a808-d3755b9bb69a"}
        r = requests.get(url, headers=header,params={"limit": 500, "page": i+1})
        res=r.json()
        elapsed=res["status"]['elapsed']
        update_time=res["status"]['timestamp']
        a=a+res["data"]
    with open('json_data.json', 'w') as outfile:
        json.dump(a, outfile)
    return [update_time,elapsed]

get_json_data()

with open('json_data.json') as json_file:
    data = json.load(json_file)


dic={}
for i in data:
    dic[i["symbol"]]=i["metrics"]

dic["BNK"].keys()



