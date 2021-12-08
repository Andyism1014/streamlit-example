import altair as alt
import math
import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as components




def set_beta():
    st.header("Market Information")
    df2=pd.read_csv("mas.csv",index_col="symbol")
    name=["metrics.marketcap.current_marketcap_usd","metrics.marketcap.liquid_marketcap_usd","metrics.supply.y_plus10_issued_percent","metrics.supply.y_2050_issued_percent","metrics.market_data.price_usd",'metrics.market_data.real_volume_last_24_hours',"metrics.all_time_high.price","metrics.all_time_high.at","metrics.risk_metrics.sharpe_ratios.last_30_days","metrics.risk_metrics.sharpe_ratios.last_90_days","metrics.roi_data.percent_change_btc_last_1_week","metrics.roi_data.percent_change_btc_last_1_month","metrics.roi_data.percent_change_btc_last_3_months","metrics.risk_metrics.sharpe_ratios.last_1_year","metrics.risk_metrics.volatility_stats.volatility_last_30_days","metrics.risk_metrics.volatility_stats.volatility_last_90_days","metrics.risk_metrics.volatility_stats.volatility_last_1_year"]
    df2=df2[name]
    st.write(df2)




