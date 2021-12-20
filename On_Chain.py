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
  df=pd.json_normalize(res.json(),sep="_")
  return df.tail(g)


@st.experimental_memo
def show_cp(dfd,dfp):
  # Create a selection that chooses the nearest point & selects based on x-value
  nearest = alt.selection(type='single', nearest=True, on='mouseover',
                          fields=['t'], empty='none')

  line1=alt.Chart(dfd).mark_line(color='#5276A7',opacity=1).transform_window(
    v='mean(v)',
    frame=[-15, 15]
).encode(
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

@st.experimental_memo
def show_cp2(df,dfp,l):
  line1=alt.Chart(df).transform_fold(
      l
  ).mark_area(opacity=0.7).encode(
      x=alt.X("t:T"),
      y=alt.Y('value:Q',axis=alt.Axis(format="s",title=None),scale=alt.Scale(zero=False)),
      color="key:N"
      )

  line2=alt.Chart(dfp).mark_line(color='#57A44C',opacity=0.5).encode(
      x=alt.X("t:T",axis=alt.Axis(title=None)),
      y=alt.Y('v:Q',axis=alt.Axis(format="s",title="price",titleColor='#57A44C'),scale=alt.Scale(zero=False))
  )

  res=alt.layer(line2,line1).resolve_scale(
          y ='independent').properties(
      width=1200, height=600
  ).interactive(bind_y=False)
  return res


def main():
    age = st.slider('Days', 0, 10000, 300)
    dfp=get_g("BTC","/v1/metrics/market/price_usd_close","24h",age)
    st.header("Active Entities（活跃个体）")
    st.write(show_cp(get_g("BTC","/v1/metrics/entities/active_count","24h",age),dfp))
    st.header("Total Transfer Volume Breakdown by Size (Entity-Adjusted)（不同交易规模的日交易量）")
    l1=st.multiselect("select",['o_vol_0_to_1k', 'o_vol_100k_to_1m', 'o_vol_10k_to_100k','o_vol_10m_plus', 'o_vol_1k_to_10k', 'o_vol_1m_to_10m'],['o_vol_0_to_1k','o_vol_100k_to_1m',"o_vol_10k_to_100k","o_vol_1k_to_10k","o_vol_1m_to_10m",'o_vol_10m_plus'])
    st.write(show_cp2(get_g("BTC","/v1/metrics/transactions/transfers_volume_by_size_entity_adjusted_sum","24h",age),dfp,l1))
    st.header("Realized Cap HODL Waves（BTC币龄分布）")
    l2=st.multiselect("select",['o_1d_1w', 'o_1m_3m', 'o_1w_1m', 'o_1y_2y', 'o_24h', 'o_2y_3y','o_3m_6m', 'o_3y_5y', 'o_5y_7y', 'o_6m_12m', 'o_7y_10y', 'o_more_10y'],['o_1d_1w', 'o_1m_3m', 'o_1w_1m', 'o_1y_2y', 'o_24h', 'o_2y_3y','o_3m_6m', 'o_3y_5y', 'o_5y_7y', 'o_6m_12m', 'o_7y_10y', 'o_more_10y'])
    st.write(show_cp2(get_g("BTC","/v1/metrics/supply/rcap_hodl_waves","24h",age),dfp,l2))
    st.header("Futures Open Interest Perpetual（永续合约持仓金额）")
    st.write(show_cp(get_g("BTC","/v1/metrics/derivatives/futures_open_interest_perpetual_sum","24h",age),dfp))
    st.header("Futures Open Interest（交割合约持仓金额）")
    st.write(show_cp(get_g("BTC","/v1/metrics/derivatives/futures_open_interest_sum","24h",age),dfp))
    st.header("Number of Whales（巨鲸人数）")
    st.write(show_cp(get_g("BTC","/v1/metrics/entities/min_1k_count","24h",age),dfp))
    st.header("Supply Held by Entities（1K-10K巨鲸持仓量")
    l3=st.multiselect("select",['o_0001_001', 'o_001_01', 'o_01_1', 'o_100_1k', 'o_10_100','o_10k_100k', 'o_1_10', 'o_1k_10k', 'o_above_100k', 'o_less_0001'],["o_1k_10k","o_10k_100k","o_above_100k"])
    st.write(show_cp2(get_g("BTC","/v1/metrics/entities/supply_distribution_relative","24h",age),dfp,l3))
    st.header("Futures Perpetual Funding Rate（资金费率）")
    st.write(show_cp(get_g("BTC","/v1/metrics/derivatives/futures_funding_rate_perpetual","24h",age),dfp))
    st.header("Futures Estimated Leverage Ratio（杠杆率）")
    st.write(show_cp(get_g("BTC","/v1/metrics/derivatives/futures_estimated_leverage_ratio","24h",age),dfp))
    st.header("Stablecoin Supply Ratio（交易所BTC与稳定币比值）")
    st.write(show_cp(get_g("BTC","/v1/metrics/indicators/ssr","24h",age)[["t","o_v"]].rename(columns={"o_v":"v"}),dfp))