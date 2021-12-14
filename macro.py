import altair as alt
import math
import pandas as pd
import requests
import streamlit as st
import time





def main():
    placeholder = st.empty()
    start_button = st.empty()
    if start_button.button('Start',key='start'):
        start_button.empty()
        if st.button('Stop',key='stop'):
            pass
        while True:
            st.write("gg")
            time.sleep(0.5)


