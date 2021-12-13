import altair as alt
import math
import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as components
import base64





def main():
    st.write(
        f'<iframe src="https://studio.glassnode.com/trading_view"></iframe>',
        unsafe_allow_html=True,
    )
