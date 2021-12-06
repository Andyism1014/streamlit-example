from os import strerror
import pandas as pd
import streamlit as st
from PIL import Image
from Portfolio import *
from ETF import *
from Portfolio2 import *
import time

im = Image.open("logo.png")
st.set_page_config(page_title='Tensor Data Platform',  layout='wide', page_icon=im)  # this needs to be the first Streamlit command



st.sidebar.image('logo.png', width=200)
st.sidebar.title('Tensor Data Platform')
st.sidebar.markdown('Alpha')
st.sidebar.header('Navigation')

options = st.sidebar.radio('Select a page:', 
    ['Home', 'Portfolio Information', 'Categories Information', 'ETF Information'])

st.sidebar.markdown('---')
st.sidebar.write('Tensor Investment Corporation')

#layout
if options=="Home":
    st.write('Tensor Investment Corporation')
    crrucy = st.text_input('Movie title', 'Life of Brian')
    st.write('The current movie title is', crrucy)

if options == 'Portfolio Information':
    set_Portfolio2()
if options == 'ETF Information':
    set_ETF()





