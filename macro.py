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
    if st.button('Start',key='start'):
        st.write(txt)



