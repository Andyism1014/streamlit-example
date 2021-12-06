from os import strerror
import pandas as pd
import streamlit as st
from PIL import Image
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
    st.title('Consolidated Volume 查询器')
    crrucy = st.text_input('输入您想查询的币种', 'BTC')
    st.write(crrucy+"Consolidated Volume")
    st.write(PaintVP(getinfor(crrucy))[0])
    st.write(PaintVP(getinfor(crrucy))[1])
if options == 'Portfolio Information':
    set_Portfolio2()
if options == 'ETF Information':
    set_ETF()





