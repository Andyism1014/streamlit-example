import requests
import pandas as pd
import numpy as np
import time
import altair as alt
import streamlit.components.v1 as components

def tvrtg(a,b):
    a=a.upper()
    b=b.upper()
    res=components.html(
        """
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
    <div id="tradingview_a94ef"></div>
    <div class="tradingview-widget-copyright"><a href="https://in.tradingview.com/symbols/%sUSDT/?exchange=%s" rel="noopener" target="_blank"><span class="blue-text">%sUSDT Chart</span></a> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    <script type="text/javascript">
    new TradingView.widget(
    {
    "width": 980,
    "height": 610,
    "symbol": "%sUSDT",
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
        """%(a,b,a,a),
        height=610, width=980
    )
    return res