import requests
import pandas as pd
import numpy as np
import time
import altair as alt
import streamlit.components.v1 as components

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
    height=1080, width=1920
)