import altair as alt
import math
import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as components



def main():
    st.write("try")
    uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
    if uploaded_file is not None:
        st.write(uploaded_file)

