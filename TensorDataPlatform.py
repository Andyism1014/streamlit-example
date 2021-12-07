from os import strerror, write
import pandas as pd
import streamlit as st
from PIL import Image
from ETF import *
from Portfolio2 import *
from beta import *
import time


im = Image.open("logo.png")
st.set_page_config(page_title='Tensor Data Platform',  layout='wide', page_icon=im)  # this needs to be the first Streamlit command
t1, t2 = st.columns((0.12,1))
t1.image('logo.png', width=155)
t2.title('Tensor Data Platform')
t2.markdown("Tensor Investment Corporation | Proprietary trading and alternative investment firm")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
st.write('Navigation')
#layout
col1, col2, col3,col4 = st.columns(4)
if col1.button("Portfolio Information"):
    set_Portfolio()
if col2.button("ETF Information"):
    set_ETF()
if col3.button("Beta"):
    set_Portfolio()
if col4.button("Function"):
    st.title('Tensor Investment Corporation')
    Choice=st.selectbox("选择功能页",("Consolidated Volume 查询器","others"))
    if Choice=="Consolidated Volume 查询器":
        st.header('Consolidated Volume 查询器')
        crrucy = st.text_input('输入您想查询的币种', 'BTC')
        st.header(crrucy.upper()+"  Consolidated Volume")
        st.write(PaintVP(getinfor(crrucy))[0])
        st.write(PaintVP(getinfor(crrucy))[1])
    if Choice=="others":
        st.write("Coming soon")






