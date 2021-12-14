import altair as alt
import math
import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as components
import base64





def main():
    components.iframe("https://studio.glassnode.com/workbench/4e473fa5-6bbb-4a50-7532-39677ab4c343",
    height=1070,width=1700)
    txt = st.text_area('Text to analyze', '''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it was
     the epoch of belief, it was the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair, (...)
     ''')
    st.write(txt)
    file1 = open('read.txt', 'w')
    print(file1.read()) 
    file1.close()
