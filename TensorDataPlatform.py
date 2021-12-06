from os import strerror
import pandas as pd
import streamlit as st
from PIL import Image
from ETF import *
from Portfolio2 import *
import time
import streamlit.components.v1 as components

im = Image.open("logo.png")
st.set_page_config(page_title='Tensor Data Platform',  layout='wide', page_icon=im)  # this needs to be the first Streamlit command



st.sidebar.image('logo.png', width=200)
st.sidebar.title('Tensor Data Platform')
st.sidebar.markdown('Alpha')
st.sidebar.header('Navigation')

options = st.sidebar.radio('Select a page:', 
    ['Home', 'Portfolio Information', 'Categories Information', 'ETF Information'])

st.sidebar.markdown('---')
st.sidebar.write('Tensor Investment Corporation')

#layout
if options=="Home":
    st.title('Tensor Investment Corporation')
    Choice=st.selectbox("选择功能页",("Consolidated Volume 查询器","others"))
    if Choice=="Consolidated Volume 查询器":
        st.header('Consolidated Volume 查询器')
        crrucy = st.text_input('输入您想查询的币种', 'BTC')
        st.header(crrucy+"  Consolidated Volume")
        st.write(PaintVP(getinfor(crrucy))[0])
        st.write(PaintVP(getinfor(crrucy))[1])
    if Choice=="others":
        st.write("Coming soon")
if options == 'Portfolio Information':
    set_Portfolio2()
if options == 'ETF Information':
    set_ETF()
if options=='Categories Information':
    components.html(
        """
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
    <div id="tradingview_a94ef"></div>
    <div class="tradingview-widget-copyright"><a href="https://in.tradingview.com/symbols/BTCUSDT/?exchange=BINANCE" rel="noopener" target="_blank"><span class="blue-text">%sUSDT Chart</span></a> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    <script type="text/javascript">
    new TradingView.widget(
    {
    "width": 980,
    "height": 610,
    "symbol": "BINANCE:BTCUSDT",
    "interval": "D",
    "timezone": "Etc/UTC",
    "theme": "dark",
    "style": "1",
    "locale": "in",
    "toolbar_bg": "#f1f3f6",
    "enable_publishing": false,
    "allow_symbol_change": true,
    "container_id": "tradingview_a94ef"
    }
    );
    </script>
    </div>
    <!-- TradingView Widget END -->
        <!-- TradingView Widget END -->
        """%("BTC"),
        height=980, width=610
    )


