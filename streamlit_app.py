import altair as alt
import math
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")  # this needs to be the first Streamlit command

st.title("Tensor Data Platform")

st.markdown("*Check out the [article](https://www.crosstab.io/articles/staged-rollout-analysis) for a detailed walk-through!*")
x = st.slider('x')
st.write(x, 'squared is', x * x)
