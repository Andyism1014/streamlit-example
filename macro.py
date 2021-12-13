import altair as alt
import math
import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as components
import base64





def main():
    
    components.html("""
    <!-- TradingView Widget BEGIN -->
    <iframe id="tradingview_18e4a" name="tradingview_18e4a" src="/charting_library/en-tv-chart.b555c6a4.html#symbol=BTC%3AMARKETPRICEUSD&amp;interval=D&amp;studiesAccess=%7B%22type%22%3A%22black%22%2C%22tools%22%3A%5B%7B%22name%22%3A%22Ratio%22%7D%5D%7D&amp;widgetbar=%7B%22details%22%3Afalse%2C%22watchlist%22%3Afalse%2C%22watchlist_settings%22%3A%7B%22default_symbols%22%3A%5B%5D%7D%7D&amp;timeFrames=%5B%7B%22text%22%3A%2220y%22%2C%22resolution%22%3A%22D%22%2C%22title%22%3A%22All%22%7D%2C%7B%22text%22%3A%225y%22%2C%22resolution%22%3A%22D%22%7D%2C%7B%22text%22%3A%222y%22%2C%22resolution%22%3A%22D%22%7D%2C%7B%22text%22%3A%221y%22%2C%22resolution%22%3A%22D%22%7D%2C%7B%22text%22%3A%226m%22%2C%22resolution%22%3A%22D%22%7D%2C%7B%22text%22%3A%223m%22%2C%22resolution%22%3A%2260%22%7D%2C%7B%22text%22%3A%221m%22%2C%22resolution%22%3A%2260%22%7D%2C%7B%22text%22%3A%2214d%22%2C%22resolution%22%3A%2260%22%7D%2C%7B%22text%22%3A%227d%22%2C%22resolution%22%3A%2210%22%7D%2C%7B%22text%22%3A%221d%22%2C%22resolution%22%3A%2210%22%7D%5D&amp;locale=en&amp;uid=tradingview_18e4a&amp;clientId=glassnode.com&amp;userId=cus_MP54Lxl8DV9x61kq&amp;chartsStorageUrl=https%3A%2F%2Ftvstore.glassnode.com&amp;chartsStorageVer=1.1&amp;customCSS=%2Fcharting-library.css&amp;debug=false&amp;timezone=Etc%2FUTC&amp;theme=Light" frameborder="0" allowtransparency="true" scrolling="no" allowfullscreen="" style="display: block; width: 100%; height: 100%;"></iframe>
    <!-- TradingView Widget END -->
    """,
    height=550,width=700)