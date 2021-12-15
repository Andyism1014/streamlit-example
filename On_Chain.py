import requests
import pandas as pd
import numpy as np
import time
import altair as alt
import streamlit as st

@st.experimental_memo(ttl=60*60*24)
def get_g(x,y,z,g):
  API_KEY = '1zza0Y66PQqo0LoeJXRooWgj41F'
  res = requests.get("https://api.glassnode.com"+y,
      params={'a':x,"timestamp_format":"humanized",'api_key':API_KEY,"i":z})
  # convert to pandas dataframe
  df = pd.read_json(res.text)
  return df.tail(g)



@st.experimental_memo(ttl=60*60*24)
def show_cp(dfd,dfp):
  # Create a selection that chooses the nearest point & selects based on x-value
  nearest = alt.selection(type='single', nearest=True, on='mouseover',
                          fields=['t'], empty='none')

  line1=alt.Chart(dfd).mark_line(color='#5276A7',opacity=1).encode(
      x=alt.X("t:T",axis=alt.Axis(title=None)),
      y=alt.Y('v:Q',axis=alt.Axis(format="s",title=None,titleColor='#5276A7'),scale=alt.Scale(zero=False))
  )

  line2=alt.Chart(dfp).mark_line(color='#57A44C',opacity=0.5).encode(
      x=alt.X("t:T",axis=alt.Axis(title=None)),
      y=alt.Y('v:Q',axis=alt.Axis(format="s",title="price",titleColor='#57A44C'),scale=alt.Scale(zero=False))
  )
  # Transparent selectors across the chart. This is what tells us
  # the x-value of the cursor
  selectors = alt.Chart(dfd).mark_point().encode(
      x='t:T',
      opacity=alt.value(0),
  ).add_selection(
      nearest
  )

  # Draw points on the line, and highlight based on selection
  points = line1.mark_point().encode(
      opacity=alt.condition(nearest, alt.value(1), alt.value(0))
  )

  # Draw text labels near the points, and highlight based on selection
  text = line1.mark_text(align='left', dx=5, dy=-5).encode(
      text=alt.condition(nearest, 'v:Q', alt.value(' '))
  )

  # Draw a rule at the location of the selection
  rules = alt.Chart(dfd).mark_rule(color='gray').encode(
      x='t:T',
  ).transform_filter(
      nearest
  )

  res=alt.layer(line2,line1,selectors,points,rules,
    text
  ).resolve_scale(
          y ='independent').properties(
      width=1200, height=600
  ).interactive(bind_y=False)
  return res



def main():
    dfp=get_g("BTC","/v1/metrics/market/price_usd_close","24h",300)
    st.header("Active Entities（活跃个体）")
    st.write(show_cp(get_g("BTC","/v1/metrics/entities/active_count","24h",300),dfp))
    st.header("Futures Open Interest Perpetual（永续合约持仓金额）")
    st.write(show_cp(get_g("BTC","/v1/metrics/derivatives/futures_open_interest_perpetual_sum","24h",300),dfp))
    st.header("Futures Open Interest（交割合约持仓金额）")
    st.write(show_cp(get_g("BTC","/v1/metrics/derivatives/futures_open_interest_sum","24h",300),dfp))
    st.header("Number of Whales（巨鲸人数）")
    st.write(show_cp(get_g("BTC","/v1/metrics/entities/min_1k_count","24h",300),dfp))
    st.header("Futures Perpetual Funding Rate（资金费率）")
    st.write(show_cp(get_g("BTC","/v1/metrics/derivatives/futures_funding_rate_perpetual","24h",300),dfp))
    st.header("Futures Estimated Leverage Ratio（杠杆率）")
    st.write(show_cp(get_g("BTC","/v1/metrics/derivatives/futures_estimated_leverage_ratio","24h",300),dfp))
    