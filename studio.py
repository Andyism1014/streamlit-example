import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import requests
import streamlit as st
from plotly.subplots import make_subplots
from datetime import datetime
from streamlit_plotly_events import plotly_events


@st.experimental_memo(ttl=60 * 60 * 12)
def get_g(symbol, addresses, intervel, currency):
    api_key = '23MchBnJN7t78kXEq0p9Hx1znTu'
    res = requests.get("https://api.glassnode.com" + addresses,
                       params={'a': symbol, 'api_key': api_key, "i": intervel, "c": currency})
    # convert to pandas dataframe
    df = pd.json_normalize(res.json(), sep="_")
    df["t"] = pd.to_datetime(df["t"], unit="s").dt.date
    return df


update_menus = [
    dict(
        type="dropdown",
        direction="down",
        yanchor="bottom",
        y=1.05,
        xanchor="right",
        x=0.985,
        buttons=list([
            dict(
                args=[{'yaxis2.type': 'linear'}],
                label="Linear Scale",
                method="relayout"
            ),
            dict(
                args=[{'yaxis2.type': 'log'}],
                label="Log Scale",
                method="relayout"
            )
        ])
    ), ]


@st.experimental_memo(ttl=60 * 60 * 12)
def layout_update(fig, title, symbol):
    fig.update_layout(
        yaxis=dict(
            autorange=True,
            fixedrange=False,
            tickfont=dict(
                color="#1f77b4"
            )
        ),
        yaxis3=dict(
            tickfont=dict(
                color='#29a329'
            ),
            anchor="free",
            overlaying="y",
            side="left",
            position=0.025
        ),
        yaxis2=dict(
            autorange=True,
            fixedrange=False,
            tickfont=dict(
                color='rgba(120, 120, 120,1)'
            ),
            anchor="x",
            overlaying="y",
            side="right"
        ),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.05,
            xanchor="left",
            x=0
        )
    )
    fig.update_layout(
        title_text=symbol + " " + title
    )
    fig.update_layout(
        updatemenus=update_menus
    )


about_market = [['Active Entities', 'BTC', '/v1/metrics/entities/active_count', '24h', 'NATIVE', 7],
                ['Gas Price (Median)', 'ETH', '/v1/metrics/fees/gas_price_median', '24h', 'NATIVE', 14],
                ['Total Transfer Volume by Size (Entity-Adjusted)', 'BTC',
                 '/v1/metrics/transactions/transfers_volume_by_size_entity_adjusted_sum', '24h', 'USD', 7],
                ['Exchange Balance (Total)', 'BTC', '/v1/metrics/distribution/balance_exchanges', '24h', 'NATIVE', 7],
                ['Number of Whales', 'BTC', '/v1/metrics/entities/min_1k_count', '24h', 'NATIVE', 1],
                ['Supply Held by Entities with Balance 1k - 10k', 'BTC', '/v1/metrics/entities/supply_balance_1k_10k',
                 '24h', 'NATIVE', 1], ['Supply Held by Entities with Balance 10k - 100k', 'BTC',
                                       '/v1/metrics/entities/supply_balance_10k_100k', '24h', 'NATIVE', 1],
                ['Exchange Balance (Total)', 'ETH', '/v1/metrics/distribution/balance_exchanges', '24h', 'NATIVE', 7],
                ['Supply Held by Addresses with Balance > 100k', 'ETH',
                 '/v1/metrics/addresses/supply_balance_more_100k',
                 '24h', 'NATIVE', 1],
                ['Supply Held by Addresses with Balance 1k - 10k', 'ETH', '/v1/metrics/addresses/supply_balance_1k_10k',
                 '24h', 'NATIVE', 1], ['Supply Held by Addresses with Balance 10k - 100k', 'ETH',
                                       '/v1/metrics/addresses/supply_balance_10k_100k', '24h', 'NATIVE', 1],
                ['Realized Cap HODL Waves ', 'BTC', '/v1/metrics/supply/rcap_hodl_waves', '24h', 'NATIVE', 14],
                ['Relative Long/Short-Term Holder Supply', 'BTC', '/v1/metrics/supply/lth_sth_profit_loss_relative',
                 '24h', 'NATIVE', 7]]

aboutderiva = [
    ['Futures Open Interest Perpetual', 'BTC', '/v1/metrics/derivatives/futures_open_interest_perpetual_sum', '24h',
     'USD', 7],
    ['Futures Volume Perpetual', 'BTC', '/v1/metrics/derivatives/futures_volume_daily_perpetual_sum', '24h', 'USD', 7],
    ['Futures Open Interest Perpetual', 'ETH', '/v1/metrics/derivatives/futures_open_interest_perpetual_sum', '24h',
     'USD', 7],
    ['Futures Volume Perpetual', 'ETH', '/v1/metrics/derivatives/futures_volume_daily_perpetual_sum', '24h', 'USD', 7],
    ['Futures Perpetual Funding Rate', 'BTC', '/v1/metrics/derivatives/futures_funding_rate_perpetual', '24h', 'NATIVE',
     1], ['Futures Estimated Leverage Ratio', 'BTC', '/v1/metrics/derivatives/futures_estimated_leverage_ratio', '24h',
          'NATIVE', 1], ['Perp OI / Market Cap', 'BTC', '', '', '', 14],
    ['Perp OI / Market Cap', 'ETH', '', '', '', 14],
    ['Stablecoin Supply Ratio (SSR)', 'BTC', '/v1/metrics/indicators/ssr', '24h', 'NATIVE', 7],
    ['Circulating Supply', 'USDC', '/v1/metrics/supply/current', '24h', 'USD', 7],
    ['Circulating Supply', 'USDT', '/v1/metrics/supply/current', '24h', 'USD', 7]]


def fenlei(listofgg):
    col1, col2 = st.columns(2)
    for i in listofgg:
        if listofgg.index(i) % 2 != 0:
            with col2:
                picture(i)
        else:
            with col1:
                picture(i)


config = {'displaylogo': False, 'modeBarButtonsToRemove': ["zoomIn", "zoomOut", "autoScale", "resetScale"],
          'modeBarButtonsToAdd': ['drawline', 'drawopenpath', 'drawrect', 'eraseshape'], }


@st.experimental_memo(ttl=60 * 60 * 12)
def addpriceline(symbol, fig, df):
    df2 = get_g(symbol, "/v1/metrics/market/price_usd_close", "24h", "NATIVE")
    df3 = df2.tail(len(df))
    name = "Price"
    fig.add_trace(go.Scatter(
        x=df3["t"],
        y=df3["v"],
        name=name,
        line=dict(color='rgba(120, 120, 120,0.5)'
                  ),
        yaxis="y2"
    ))


glistdic = {"Stablecoin Supply Ratio (SSR)": ["o_v"],
            "Relative Transfer Volume by Size (Entity-Adjusted)": ['o_vol_10m_plus', 'o_vol_1m_to_10m',
                                                                   'o_vol_100k_to_1m', 'o_vol_10k_to_100k',
                                                                   'o_vol_1k_to_10k', 'o_vol_0_to_1k'],
            "Total Transfer Volume by Size (Entity-Adjusted)": ['o_vol_10m_plus', 'o_vol_1m_to_10m', 'o_vol_100k_to_1m',
                                                                'o_vol_10k_to_100k', 'o_vol_1k_to_10k',
                                                                'o_vol_0_to_1k'],
            "Relative Long/Short-Term Holder Supply": ["o_lth_profit", "o_lth_loss", "o_sth_loss", "o_sth_profit"],
            "Realized Cap HODL Waves ": ["o_24h", "o_1d_1w", "o_1w_1m", "o_1m_3m", "o_3m_6m", "o_6m_12m", "o_1y_2y",
                                         "o_2y_3y", "o_3y_5y", "o_5y_7y", "o_7y_10y", "o_more_10y"]}

color_list = {"o_vol_0_to_1k": "#ff4b5f", "o_vol_1k_to_10k": "#ff9127", "o_vol_10k_to_100k": "#ffd300",
              "o_vol_100k_to_1m": "#a2ff38", "o_vol_1m_to_10m": "#00e376", "o_vol_10m_plus": "#00cfba",
              'o_1d_1w': 'rgba(210,90,117,255)', 'o_1m_3m': 'rgba(251,157,86,255)', 'o_1w_1m': 'rgba(239,100,69,255)',
              'o_1y_2y': 'rgba(245,250,173,255)', 'o_24h': 'rgba(158,1,66,255)', 'o_2y_3y': 'rgba(206,237,156,255)',
              'o_3m_6m': 'rgba(254,206,121,255)', 'o_3y_5y': 'rgba(152,214,164,255)',
              'o_5y_7y': 'rgba(152,214,175,255)', 'o_6m_12m': 'rgba(254,237,154,255)',
              'o_7y_10y': 'rgba(71,186,174,255)', 'o_more_10y': 'rgba(49,132,188,255)', 'o_lth_loss': '#4F92F6',
              'o_lth_profit': '#004AFF', 'o_sth_loss': '#F75F5F', 'o_sth_profit': '#FF0000', "BTC": "#f7931a",
              "ETH": "#647cec", "USDC": "#0362fc", "USDT": "#03fc41"}


@st.experimental_memo
def elementcheck(df, two):
    l = df.columns[1:].tolist()
    if len(l) == 1:
        return l
    else:
        l = glistdic[two]
        return l


def addtrace(df, listy, fig, slider, name, axis, symbol):
    if len(listy) == 1:
        fig.add_trace(go.Scatter(
            x=df["t"],
            y=df[listy[0]].rolling(slider).mean(),
            name=name,
            line=dict(color=color_list[symbol]),
            yaxis="y" + str(axis)
        ))
    else:
        for i in listy:
            fig.add_trace(go.Scatter(
                x=df["t"],
                y=df[i].rolling(slider).mean(),
                line=dict(width=0.5, color=color_list[i]),
                name=i,
                stackgroup='one',
                yaxis="y1"
            ))


timeperiod = ["6m", "1y", "3y", "all"]
timeconvertor = {"6m": 180, "1y": 365, "3y": 900, "all": 4380}


def picture(l):
    two, symbol, addresses, intervel, currency, movingaverage = l[0], l[1], l[2], l[3], l[4], l[5]
    if two == "Perp OI / Market Cap":
        PerpOI(symbol)
    else:
        fig = go.Figure()
        with st.expander("Setting"):
            st.write(two)
            slider = st.number_input("MovingAverage", min_value=1, max_value=100, step=1, value=movingaverage,
                                     key=symbol + two)
            numberofdata = st.selectbox("Timeperiod", timeperiod, key=symbol + two)
        df = get_g(symbol, addresses, intervel, currency).tail(timeconvertor[numberofdata])
        listy = elementcheck(df, two)
        addtrace(df, listy, fig, int(slider), two, 1, symbol)
        addpriceline(symbol, fig, df)
        layout_update(fig, two, symbol)
        if two == "Futures Perpetual Funding Rate":
            fig.layout.yaxis.tickformat = '.3%'
        st.plotly_chart(fig, use_container_width=True, config=config)
        if two == "Realized Cap HODL Waves ":
            HODLtable(df, two)


@st.experimental_memo(ttl=60 * 60 * 24)
def messariP(x):
    today = datetime.today().strftime('%Y-%m-%d')
    url = "https://data.messari.io/api/v1/assets/%s/metrics/price/time-series" % x
    header = {"x-messari-api-key": "77fd912b-7c49-449f-a808-d3755b9bb69a"}
    r = requests.get(url, headers=header,
                     params={"start": "2021-01-01", "end": today, "interval": "1d", "columns": "close"})
    df = pd.DataFrame(r.json()["data"]["values"])
    return df


lay1 = ["SOL", "BNB", "ADA", "MATIC", "AVAX", "LUNA", "DOT", "ALGO", "TRX", "FTM"]


def messari():
    ethp = messariP("ETH")
    fig = go.Figure()
    with st.expander("Edit"):
        slider = st.slider("Moving average", min_value=1, max_value=100, step=1, key=0)
    for i in lay1:
        df = messariP(i)
        df[1] = df[1] / ethp[1]
        df[1] = df[1].pct_change()
        df[1] = df[1] + 1
        df[1] = df[1].cumprod()
        df[0] = pd.to_datetime(df[0], unit="ms").dt.date
        fig.add_trace(go.Scatter(
            x=df[0],
            y=df[1].rolling(slider).mean(),
            name=i
        ))
    fig.update_layout(
        yaxis=dict(tickformat=".2%"),
        title_text="Layer 1 in ETH",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.05,
            xanchor="left",
            x=0
        )
    )
    st.plotly_chart(fig, use_container_width=True, config=config)


def PerpOI(sym):
    l = ["Futures Open Interest Perpetual", sym, "/v1/metrics/derivatives/futures_open_interest_perpetual_sum", "24h",
         "USD"]
    df4 = get_g(sym, "/v1/metrics/market/marketcap_usd", "24h", "NATIVE")
    two, symbol, addresses, intervel, currency = l[0], l[1], l[2], l[3], l[4]
    fig = go.Figure()
    with st.expander("Setting"):
        numberofdata = st.selectbox("Timeperiod", timeperiod, key=symbol + "Perp OI / Market Cap")
    df = get_g(symbol, addresses, intervel, currency).tail(timeconvertor[numberofdata]).reset_index()
    df4 = df4.tail(len(df)).reset_index()
    df4["v"] = 100 * df["v"] / df4["v"]
    fig.add_trace(go.Scatter(
        x=df["t"],
        y=df["v"],
        name=two,
        yaxis="y1"
    ))
    fig.add_trace(go.Scatter(
        x=df4["t"],
        y=df4["v"],
        name="Perp OI / Market Cap",
        yaxis="y3"
    ))
    fig.add_shape(type='line',
                  x0=min(df4["t"]),
                  y0=1.3,
                  x1=max(df4["t"]),
                  y1=1.3,
                  line=dict(color='Black', ),
                  xref='x',
                  yref='y3'
                  )
    addpriceline(symbol, fig, df)
    layout_update(fig, "Perp OI / Market Cap", symbol)
    st.plotly_chart(fig, use_container_width=True, config=config)


@st.experimental_memo(ttl=60 * 60 * 24)
def getbinancefutures(addrece, name):
    r = requests.get(" https://fapi.binance.com" + addrece, params={"limit": 30, "period": "1d", "symbol": name})
    df = pd.read_json(r.text)
    return df


listoffuturesdata = ["/futures/data/openInterestHist", "/futures/data/topLongShortAccountRatio",
                     "/futures/data/topLongShortPositionRatio", "/futures/data/globalLongShortAccountRatio"]

listoffuturesdatalegend = {"/futures/data/openInterestHist": ["持仓总数量", "持仓总价值"],
                           "/futures/data/topLongShortAccountRatio": ["大户多仓账户数比例", "大户多仓账户数比值", "大户空仓账户数比例"],
                           "/futures/data/topLongShortPositionRatio": ["大户多仓持仓量比例", "大户多空持仓量比值", "大户空仓持仓量比例"],
                           "/futures/data/globalLongShortAccountRatio": ["多仓人数比例", " 多空人数比值", "空仓人数比例"]}

longshortcolor = {"longAccount": "#2cbc84", "shortAccount": "#e22d4c", "sumOpenInterest": "#83afdd"}


def longshortRatio():
    with st.expander("Setting"):
        name = st.selectbox("symbol", ["BTCUSDT", "ETHUSDT"])
    r = requests.get("https://api.binance.com/api/v3/klines", params={"limit": 30, "interval": "1d", "symbol": name})
    df = pd.read_json(r.text)
    df[0] = pd.to_datetime(df[0], unit="ms").dt.date
    fig = make_subplots(
        rows=5, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.08,
        subplot_titles=(name, "合约持仓量", "大户账户数多空比", "大户持仓量多空比", "多空持仓人数比"),
        specs=[[{"secondary_y": True}],
               [{"secondary_y": True}],
               [{"secondary_y": True}],
               [{"secondary_y": True}],
               [{"secondary_y": True}]]
    )
    fig.add_trace(go.Candlestick(x=df[0],
                                 open=df[1],
                                 high=df[2],
                                 low=df[3],
                                 close=df[4],
                                 name="Price"
                                 ),
                  row=1, col=1
                  )
    for i in listoffuturesdata:
        legendname = listoffuturesdatalegend[i]
        rownumber = listoffuturesdata.index(i) + 2
        df = getbinancefutures(i, name)
        keyelement = list(df.columns)[1:-1]
        for j in keyelement:
            numberofj = keyelement.index(j)
            if numberofj == 1:
                fig.add_trace(go.Scatter(
                    x=df["timestamp"],
                    y=df[j],
                    mode='lines+markers',
                    line=dict(color='#4c525d'
                              ),
                    name=legendname[numberofj]
                ),
                    row=rownumber, col=1, secondary_y=True
                )
            else:
                fig.add_trace(go.Bar(
                    x=df["timestamp"],
                    y=df[j],
                    marker_color=longshortcolor[j],
                    name=legendname[numberofj]
                ),
                    row=rownumber, col=1, secondary_y=False
                )
    fig.update_layout(
        title_text=name + " " + "币安衍生品数据"
    )
    fig.update_layout(hovermode="x unified", barmode='stack', showlegend=False, height=1200)
    fig.update_layout(xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True, config=config)


@st.experimental_memo(ttl=60 * 60 * 24, show_spinner=False)
def redataURPD(df):
    list_value = []
    for i in range(len(df)):
        current_price = df.iloc[i]["current_price"]
        ath_price = df.iloc[i]["ath_price"]
        total_supply = df.iloc[i]["total_supply"]
        temp = 0
        ap = df.iloc[i]["partitions"][0] / total_supply
        for j in range(1, 100):
            ap = ap + df.iloc[i]["partitions"][j] / total_supply
            temp = int(temp + ath_price / 100) + int(ath_price) * 10 ** (-len(str(int(ath_price))))
            if (temp + ath_price / 100) > current_price > temp:
                a = [str(df.iloc[i]["t"]), "T", temp, df.iloc[i]["partitions"][j],
                     df.iloc[i]["partitions"][j] / total_supply, ap]
            else:
                if ap <= 0.25:
                    a = [str(df.iloc[i]["t"]), "F1", temp, df.iloc[i]["partitions"][j],
                         df.iloc[i]["partitions"][j] / total_supply, ap]
                elif 0.25 < ap <= 0.5:
                    a = [str(df.iloc[i]["t"]), "F2", temp, df.iloc[i]["partitions"][j],
                         df.iloc[i]["partitions"][j] / total_supply, ap]
                elif 0.5 < ap <= 0.75:
                    a = [str(df.iloc[i]["t"]), "F3", temp, df.iloc[i]["partitions"][j],
                         df.iloc[i]["partitions"][j] / total_supply, ap]
                else:
                    a = [str(df.iloc[i]["t"]), "F4", temp, df.iloc[i]["partitions"][j],
                         df.iloc[i]["partitions"][j] / total_supply, ap]
            list_value.append(a)
    df2 = pd.DataFrame(list_value, columns=['t', "color", 'Price', 'Distribution', "Percentage", "AP"])
    return df2


@st.experimental_memo(ttl=60 * 60 * 24, show_spinner=False)
def URPDgraph(df2):
    fig = px.bar(df2, x="Price", y="Percentage", color="color", animation_frame="t", hover_name="t",
                 hover_data={"color": False, "t": False, "Percentage": ":.2%", "AP": ":.2%"})
    fig.update_layout(
        title_text="UTXO Realized Price Distribution (URPD)", showlegend=False
    )
    return fig


def URPD():
    l = ["URPD (ATH-Partitioned) ", "BTC", "/v1/metrics/indicators/utxo_realized_price_distribution_ath", "24h",
         "NATIVE", 1]
    two, symbol, addresses, intervel, currency, movingaverage = l[0], l[1], l[2], l[3], l[4], l[5]
    with st.expander("Setting"):
        numberofdata = st.selectbox("Timeperiod", timeperiod, key="UTXO Realized Price Distribution (URPD)")
    df = get_g(symbol, addresses, intervel, currency).tail(timeconvertor[numberofdata])
    df2 = redataURPD(df)
    fig = URPDgraph(df2)
    fig.layout.yaxis.tickformat = '.1%'
    selectedpoints = plotly_events(fig, click_event=False, select_event=True)
    if len(selectedpoints) == 0:
        selected_points = [
            {
                "x": 37097.68642,
                "y": 0.007648795825883361,
                "curveNumber": 2,
                "pointNumber": 37,
                "pointIndex": 37
            }
        ]
    else:
        selected_points = selectedpoints
    small_quant = int(str(selected_points[0]["x"]).split(".")[1]) / 200
    df3 = df2.loc[(int(selected_points[-1]["x"] + small_quant) > df2["Price"])
                  & (int(selected_points[0]["x"] - small_quant) < df2["Price"])]
    time = df3["t"].unique()
    changeofpercentage = []
    for i in time:
        changeofpercentage.append(df3.loc[df3["t"] == i]["Percentage"].sum())
    df4 = pd.DataFrame({"t": time, "v": changeofpercentage})
    fig2 = go.Figure()
    with st.expander("Setting"):
        slider = st.number_input("MovingAverage", min_value=1, max_value=100, step=1, value=movingaverage,
                                 key=symbol + two)
    st.write("Range from " + str(int(selected_points[0]["x"] - small_quant)) + " to "
             + str(int(selected_points[-1]["x"] + small_quant)))
    listy = ["v"]
    addtrace(df4, listy, fig2, int(slider), "URPD", 1, symbol)
    addpriceline(symbol, fig2, df4)
    layout_update(fig2, two, symbol)
    fig2.update_layout(hovermode="x unified")
    fig2.layout.yaxis.tickformat = '.1%'
    st.plotly_chart(fig2, use_container_width=True, config=config)


def URPD2():
    st.write("")


def HODLtable(df, two):
    df = df.set_index("t")
    with st.expander("Setting"):
        timechoose = st.date_input("Start", list(df.index)[-11], min_value=list(df.index)[0],
                                   max_value=list(df.index)[-1], key="timechoose")
        timechoose2 = st.date_input("End", list(df.index)[-1], min_value=list(df.index)[0],
                                    max_value=list(df.index)[-1], key="timechoose2")
    df = df[glistdic[two]]
    a = df.loc[timechoose].to_list()
    b = df.loc[timechoose2].to_list()
    c = df.loc[timechoose2] - df.loc[timechoose]
    c = c.round(3)
    d = c.to_list()
    font_color = ['rgb(40,40,40)', 'rgb(40,40,40)', 'rgb(40,40,40)',
                  ["rgba(158,1,66,255)" if v < 0 else 'rgba(71,186,174,255)' for v in d]]
    fig = go.Figure(data=[go.Table(header=dict(
        values=["<b>HODL Waves<b>", "<b>" + str(timechoose) + "<b>", "<b>" + str(timechoose2) + "<b>", "<b>偏差<b>"],
        font=dict(color=['rgb(45,45,45)'] * 4, size=14)),
        cells=dict(values=[
            ["24小时", "1天至1周", "1周至1月", "1月至3月", "3月至6月", "6月至12月", "1年至2年", "2年至3年", "3年至5年",
             "5年至7年", "7年至10年", "超过10年"], a, b, d],
            font=dict(family="Arial", size=14, color=font_color),
            height=30,
            format=["", ".2%", ".2%", ".1%"]))
    ])
    fig.update_layout(autosize=False, height=575)
    st.plotly_chart(fig, use_container_width=True, config=config)
