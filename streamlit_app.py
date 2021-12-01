import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
from vega_datasets import data

st.set_page_config(layout="wide")  # this needs to be the first Streamlit command

st.title("Tensor Data Platform")


source = data.seattle_weather()

base = alt.Chart(source).encode(
    alt.X('month(date):T', axis=alt.Axis(title=None))
)

area = base.mark_area(opacity=0.3, color='#57A44C').encode(
    alt.Y('average(temp_max)',
          axis=alt.Axis(title='Avg. Temperature (°C)', titleColor='#57A44C')),
    alt.Y2('average(temp_min)')
)

line = base.mark_line(stroke='#5276A7', interpolate='monotone').encode(
    alt.Y('average(precipitation)',
          axis=alt.Axis(title='Precipitation (inches)', titleColor='#5276A7'))
)

alt.layer(area, line).resolve_scale(
    y = 'independent'
)
