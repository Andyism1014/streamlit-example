import altair as alt
import math
import pandas as pd
import requests
import streamlit as st
import time





def main():
    a=[]
    txt = st.text_area('Text to analyze', '''
    ss
     ''')
    start_button = st.empty()
    if start_button.button('Start',key='start'):
        a.append(txt)
    st.write(a)





