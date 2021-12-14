import altair as alt
import math
import pandas as pd
import requests
import streamlit as st
import time





def main():
    txt = st.text_area('Text to analyze', '''
    ss
     ''')
    start_button = st.empty()
    if start_button.button('Start',key='start'):
        start_button.empty()
        st.write(txt)



