from sqlalchemy import create_engine
import requests
import pandas as pd

engine = create_engine('sqlite:///database.db')


def expend_URPD(df):
    df3 = pd.DataFrame(df['partitions'].to_list(), columns=range(100))
    df4 = pd.concat([df[["t", "ath_price", "current_price", "total_supply"]], df3], axis=1)
    return df4


def update_g(symbol, addresses, intervel, currency):
    api_key = '23xKyUhf3J2dYGXBD2tgsYkvjrv'
    res = requests.get("https://api.glassnode.com" + addresses,
                       params={'a': symbol, 'api_key': api_key, "i": intervel, "c": currency})
    # convert to pandas dataframe
    df = pd.json_normalize(res.json(), sep="_")
    if addresses == "/v1/metrics/indicators/utxo_realized_price_distribution_ath":
        df = expend_URPD(df)
    df["t"] = pd.to_datetime(df["t"], unit="s")
    df.to_sql(symbol + addresses + intervel + currency, engine, if_exists="replace")


# %%


# %%
l = ["URPD (ATH-Partitioned) ", "BTC", "/v1/metrics/indicators/utxo_realized_price_distribution_ath", "24h",
     "NATIVE", 1]
two, symbol, addresses, intervel, currency, movingaverage = l[0], l[1], l[2], l[3], l[4], l[5]

update_g(symbol, addresses, intervel, currency)

print("good")

# %%
api_key = '23xKyUhf3J2dYGXBD2tgsYkvjrv'
res = requests.get("https://api.glassnode.com" + addresses,
                   params={'a': symbol, 'api_key': api_key, "i": intervel, "c": currency})
# convert to pandas dataframe
df = pd.json_normalize(res.json(), sep="_")

# %%

df3 = pd.DataFrame(df['partitions'].to_list(), columns=range(100))
df4 = pd.concat([df[["t", "ath_price", "current_price", "total_supply"]], df3], axis=1)
df4
# %%


# %%
