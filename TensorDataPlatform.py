import altair as alt
import pandas as pd
import streamlit as st
from PIL import Image

im = Image.open("1566968153508.png")
st.set_page_config(page_title='Tensor Data Platform',  layout='wide', page_icon=im)  # this needs to be the first Streamlit command



st.sidebar.image('1566968153508.png', width=200)
st.sidebar.title('Tensor Data Platform')
st.sidebar.markdown('version Alpha')
st.sidebar.header('Navigation')

options = st.sidebar.radio('Select a page:', 
    ['Home', 'Portfolio Information', 'Categories Information', 'Data Information'])

st.sidebar.markdown('---')
st.sidebar.write('Tensor Investment Corporation')

#layout
if options == 'Portfolio Information':
    st.header("LAT Volume")

if options == 'Home':
    st.header("CKB Volume")





