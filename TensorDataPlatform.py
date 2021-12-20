from os import strerror, write
import pandas as pd
import streamlit as st
from PIL import Image
from Portfolio import *
from On_Chain import *
import streamlit.components.v1 as components
import time

im = Image.open("logo.png")
st.set_page_config(page_title='Tensor Data Platform',  layout='wide', page_icon=im)  # this needs to be the first Streamlit command
st.markdown("""  
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark" >
<a class="navbar-brand" href="#">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAB1UExURQAAAENDQ7y8vENDQ7y8vENDQ0NDQ0VFRUdHR7q6ury8vL29vUFBQUJCQkNDQ0VFRUZGRkhISLi4uLm5ubq6ury8vL6+vkVFRUFBQUJCQkNDQ0REREVFRUZGRkdHR0hISLi4uLm5ubq6uru7u7y8vL29vb6+vpO8NMYAAAAYdFJOUwAqKjU1X5+fn5+fn8nJycnJycnJycnJ1GLIJUIAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKdSURBVHhe7dxtV5swGIDh0mJ968BZbAGLDpn9/z9x9OxBS56okKWN7e7r43DJbiDE7pwyAQAAAAAAAAAAAAAAAPA/i2ZOIvnrb3yN4yqap0krHSm5NP4F0eX4MXbzzn2VzNJHB5synckAYpaUGzk4ijmOs11IKYMOZwlJHULaiQkxuYU82kLk0AiEWLBGzjbE5fHrO2Q8TyGt73dFWCMywL9yC2Ef6Qsf8h1vrSRsSPLtQhz3EY8hZS7DjmALeSoqObqnKJ+K0vLnIi/9hSyqanyJJWSx0SGb5zIv8+LDK55X1cJXSHSVpF99SF3LvO9sIVWu7q31z/bz7N3dh5+k26mv/H1ol/8F+MSFLrHdWrl55tcXMsAnvHUMsXtEGywhVSHH3pg/E5wOsdxaP8rCvLVOMyQp1fP3NEPSjdqPTvSKbM7mihByNDrE9ms8IcfDGiHkQE4jZBorUznU8RYyYC5n09tV9rBcZvuujdF9hUyvZYK/lsuHbHXrqyS+r3/Vv/uyWA4KHeL2+I0zmaDTTn1vzOUszppt89J3uBCZoNNObc7lLF4127rp+zrE7dZqT1pfvW1W/q7IS1PLCeocLkQm6NSNmstZe5bqVzlBnaNdkdfa461lDt46WkjrbEKWXBGDW4jr41cm2EOIyS2Exa4QYiKEkL7AIewjSuAQ1ohCiIkQQvoCh7CPKIFDWCMKISZCCOkLHMI+ogQOYY0ohJgIIaQvcAj7iBI4hDWiEGIihJC+wCHsI0rgENaIQoiJEEL6AoewjyiBQ1gjCiEmQgjpCxzCPqIEDmGNKN5Cpjfy1a09N8YXuKK5vGzineU9jfodGOY7GIfM5W7IV+osL7hQL50Y8jOH/PoeAAAAAAAAAAAAAAAAAAQzmfwBINWrkHv3C28AAAAASUVORK5CYII=" width="30" height="30" class="d-inline-block align-top" alt="">
Tensor Data Platform
</a>
</nav>
""",unsafe_allow_html=True)




radio_list = ['Portfolio Information', 'On-Chain Data', 'Beta']
query_params = st.experimental_get_query_params()

# Query parameters are returned as a list to support multiselect.
# Get the first item in the list if the query parameter exists.
default = int(query_params["activity"][0]) if "activity" in query_params else 0
activity = st.radio(
    "",
    radio_list,
    index = default
)
if activity:
    st.experimental_set_query_params(activity=radio_list.index(activity))

if activity=="Portfolio Information":
  st.header("Market Information")
  k1, k2,k3= st.columns([2,1,1])
  with k1:
    components.html("""
  <!-- TradingView Widget BEGIN -->
  <div class="tradingview-widget-container">
    <div id="tradingview_ac961"></div>
    <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/BTCUSDT/?exchange=PHEMEX" rel="noopener" target="_blank"><span class="blue-text">BTC</span></a> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    <script type="text/javascript">
    new TradingView.MediumWidget(
    {
    "symbols": [
      [
        "BTC",
        "PHEMEX:BTCUSDT|1M"
      ],
      [
        "ETH",
        "BINANCE:ETHUSDT|1M"
      ]
    ],
    "chartOnly": false,
    "width": 1000,
    "height": 400,
    "locale": "en",
    "colorTheme": "light",
    "gridLineColor": "rgba(42 ,46, 57, 0)",
    "fontColor": "#787B86",
    "isTransparent": false,
    "autosize": false,
    "showFloatingTooltip": true,
    "showVolume": false,
    "scalePosition": "no",
    "scaleMode": "Normal",
    "fontFamily": "Trebuchet MS, sans-serif",
    "noTimeScale": false,
    "chartType": "area",
    "lineColor": "#2962FF",
    "bottomColor": "rgba(41, 98, 255, 0)",
    "topColor": "rgba(41, 98, 255, 0.3)",
    "container_id": "tradingview_ac961"
  }
    );
    </script>
  </div>
  <!-- TradingView Widget END -->
    """,
      height=380)
  with k2:
    components.html("""
    <!-- TradingView Widget BEGIN -->
  <div class="tradingview-widget-container">
    <div class="tradingview-widget-container__widget"></div>
    <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/markets/indices/" rel="noopener" target="_blank"><span class="blue-text">Indices</span></a> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
    {
    "colorTheme": "light",
    "dateRange": "1D",
    "showChart": false,
    "locale": "en",
    "largeChartUrl": "",
    "isTransparent": false,
    "showSymbolLogo": false,
    "showFloatingTooltip": false,
    "width": "400",
    "height": "465",
    "tabs": [
      {
        "title": "Indices",
        "symbols": [
          {
            "s": "BINANCE:BTCUSDT",
            "d": "BTC"
          },
          {
            "s": "BINANCE:ETHUSDT",
            "d": "ETH"
          },
          {
            "s": "OANDA:NAS100USD",
            "d": "NAS100"
          },
          {
            "s": "CURRENCYCOM:US500",
            "d": "S&P500"
          },
          {
            "s": "SSE:000300",
            "d": "CSI300"
          }
        ],
        "originalTitle": "Indices"
      }
    ]
  }
    </script>
  </div>
  <!-- TradingView Widget END -->
  """,height=380)
if activity=="On-Chain Data":
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



    











