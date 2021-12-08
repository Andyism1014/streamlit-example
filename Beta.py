import altair as alt
import math
import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as components




def set_beta():
    st.header("Market Information")
    df2=pd.read_csv("mas.csv",index_col="symbol")
    name=["metrics.marketcap.current_marketcap_usd","metrics.marketcap.liquid_marketcap_usd","metrics.supply.y_plus10_issued_percent","metrics.supply.y_2050_issued_percent","metrics.market_data.price_usd",'metrics.market_data.real_volume_last_24_hours',"metrics.all_time_high.price","metrics.risk_metrics.sharpe_ratios.last_30_days","metrics.risk_metrics.sharpe_ratios.last_90_days","metrics.roi_data.percent_change_btc_last_1_week","metrics.roi_data.percent_change_btc_last_1_month","metrics.roi_data.percent_change_btc_last_3_months","metrics.risk_metrics.sharpe_ratios.last_1_year","metrics.risk_metrics.volatility_stats.volatility_last_30_days","metrics.risk_metrics.volatility_stats.volatility_last_90_days","metrics.risk_metrics.volatility_stats.volatility_last_1_year",'profile.general.overview.tags']
    df2=df2[name]
    df2=df2.rename(columns={
 'metrics.all_time_high.price': 'all_time_high.price',
 'metrics.market_data.price_usd': 'price',
 'metrics.market_data.real_volume_last_24_hours': 'real_volume_last_24_hours',
 'metrics.marketcap.current_marketcap_usd': 'current_marketcap',
 'metrics.marketcap.liquid_marketcap_usd': 'liquid_marketcap',
 'metrics.risk_metrics.sharpe_ratios.last_1_year': 'sharpe_ratios.last_1_year',
 'metrics.risk_metrics.sharpe_ratios.last_30_days': 'sharpe_ratios.last_30_days',
 'metrics.risk_metrics.sharpe_ratios.last_90_days': 'sharpe_ratios.last_90_days',
 'metrics.risk_metrics.volatility_stats.volatility_last_1_year': 'volatility_last_1_year',
 'metrics.risk_metrics.volatility_stats.volatility_last_30_days': 'volatility_last_30_days',
 'metrics.risk_metrics.volatility_stats.volatility_last_90_days': 'volatility_last_90_days',
 'metrics.roi_data.percent_change_btc_last_1_month': 'Alpha_last_1_month',
 'metrics.roi_data.percent_change_btc_last_1_week': 'Alpha_last_1_week',
 'metrics.roi_data.percent_change_btc_last_3_months': 'Alpha_last_3_months',
 'metrics.supply.y_2050_issued_percent': 'y_2050_issued',
 'metrics.supply.y_plus10_issued_percent': 'y_plus10_issued',
 'profile.general.overview.tags':"tags"
 })
    s=df2.style.format(na_rep='MISSING', thousands=" ",
                    formatter={'y_2050_issued': lambda x: "{:,.2%}".format(x*0.01), 'y_plus10_issued': lambda x: "{:,.2%}".format(x*0.01),'Alpha_last_1_month': lambda x: "{:,.2%}".format(x*0.01), 'Alpha_last_1_week': lambda x: "{:,.2%}".format(x*0.01),"Alpha_last_3_months": lambda x: "{:,.2%}".format(x*0.01),
                            'current_marketcap': "$ {:,.1f}", 'liquid_marketcap': "$ {:,.1f}",'price': "$ {:,.1f}",'all_time_high.price': "$ {:,.1f}"
                            })
    st.write(s)





