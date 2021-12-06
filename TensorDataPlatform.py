from os import strerror
import pandas as pd
import streamlit as st
from PIL import Image
from ETF import *
from Portfolio2 import *
from Categories import *
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
    st.title('Tensor Investment Corporation')
    Choice=st.selectbox("选择功能页",("Consolidated Volume 查询器","others"))
    if Choice=="Consolidated Volume 查询器":
        st.header('Consolidated Volume 查询器')
        crrucy = st.text_input('输入您想查询的币种', 'BTC')
        st.header(crrucy+"  Consolidated Volume")
        st.write(PaintVP(getinfor(crrucy))[0])
        st.write(PaintVP(getinfor(crrucy))[1])
    if Choice=="others":
        st.write("Coming soon")
if options == 'Portfolio Information':
    set_Portfolio2()
if options == 'ETF Information':
    set_ETF()
if options=='Categories Information':
    tvrtg("BTC","BIANCE")


