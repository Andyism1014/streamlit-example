import streamlit as st
import hydralit_components as hc
from Portfolio import *
from studio import *

st.set_page_config(page_title='Tensor Data Platform', layout='wide')  # this needs to be the first Streamlit command

menu_data = [
    {'icon': "far fa-copy", 'label': "Portfolio"},
    {'icon': "far fa-chart-bar", 'label': "Data Overview",
     'submenu': [{'id': '市场交易结构分析', 'icon': "fa fa-database", 'label': "市场交易结构分析"},
                 {'id': '资金流与趋势分析', 'icon': "fa fa-database", 'label': "资金流与趋势分析"},
                 {'id': '币安衍生品数据', 'icon': "fa fa-database", 'label': "币安衍生品数据"},
                 {'id': 'UTXO Realized Price Distribution (URPD)', 'icon': "fa fa-database",
                  'label': "UTXO Realized Price Distribution (URPD)"}]},
    {'icon': "", 'label': "Other"}
]

over_theme = {'txc_inactive': '#FFFFFF', "menu_background": "#3d3d3d"}

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    hide_streamlit_markers=False,  # will show the st hamburger as well as the navbar now!
    sticky_nav=True,  # at the top or not
    sticky_mode='Sticky',  # jumpy or not-jumpy, but sticky or pinned
)

if menu_id == "Portfolio":
    set_Portfolio()
if menu_id == "市场交易结构分析":
    st.subheader("市场交易活跃度与交易量")
    fenlei(about_market[0:3])
    st.subheader("交易所余额")
    fenlei(about_market[3:11])
    st.subheader("BTC 长期持有者")
    fenlei(about_market[-2:])
if menu_id == "币安衍生品数据":
    longshortRatio()
if menu_id == "资金流与趋势分析":
    st.subheader("衍生品期货合约")
    fenlei(aboutderiva[0:8])
    st.subheader("稳定币")
    fenlei(aboutderiva[-3:])
if menu_id == "UTXO Realized Price Distribution (URPD)":
    st.write("UTXO Realized Price Distribution (URPD)")
    URPD()
    URPD2()

corelation_analysis = """
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
<div id="tradingview_b64c6"></div>
<div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/BTCUSDT/?exchange=BINANCE" rel="noopener" target="_blank"><span class="blue-text">BTCUSDT Chart</span></a> by TradingView</div>
<script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
<script type="text/javascript">
new TradingView.widget(
    {
        "width": 980,
        "height": 620,
        "symbol": "BINANCE:BTCUSDT",
        "interval": "60",
        "timezone": "Etc/UTC",
        "theme": "light",
        "style": "2",
        "locale": "en",
        "toolbar_bg": "#f1f3f6",
        "enable_publishing": false,
        "hide_top_toolbar": false,
        "allow_symbol_change": true,
        "save_image": false,
        "studies": [
            {"id":"CorrelationCoefficient@tv-basicstudies",
            "inputs":{
            "symbol":"OANDA:SPX500USD"
            }
            },
            {"id":"CorrelationCoefficient@tv-basicstudies",
            "inputs":{
            "symbol":"NAS100USD"
            }
            },
            {"id":"Compare@tv-basicstudies",
            "inputs":{
            "symbol":"OANDA:SPX500USD"}
             
            },
            {"id":"Compare@tv-basicstudies",
            "inputs":{
            "symbol":"NAS100USD"}
             
            }
        ],
        "container_id": "tradingview_b64c6"
    }
);
</script>
</div>
<!-- TradingView Widget END -->
"""

if f"{menu_id}" == "Other":
    components.html(corelation_analysis, height=600)
