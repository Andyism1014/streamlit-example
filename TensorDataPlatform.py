from os import strerror, write
import pandas as pd
import streamlit as st
from PIL import Image
from ETF import *
from Portfolio import *
from Beta import *
import time


im = Image.open("logo.png")
st.set_page_config(page_title='Tensor Data Platform',  layout='wide', page_icon=im)  # this needs to be the first Streamlit command
t1, t2 = st.columns((0.12,1))
t1.image('logo.png', width=155)
t2.title('Tensor Data Platform')
t2.markdown("Tensor Investment Corporation | Proprietary trading and alternative investment firm")
option = st.selectbox('Navigation',('Portfolio Information', 'ETF Information', 'Beta',"Function"))

#layout
if option=="Portfolio Information":
    set_Portfolio()
if option=="ETF Information":
    set_ETF()
if option=="Beta":
    set_beta()
if option=="Function":
    st.title('Tensor Investment Corporation')
    Choice=st.selectbox("选择功能页",("Consolidated Volume 查询器","others"))
    if Choice=="Consolidated Volume 查询器":
        st.header('Consolidated Volume 查询器')
        crrucy = st.text_input('输入您想查询的币种', 'BTC')
        set_one(crrucy)
    if Choice=="others":
        st.write("Coming soon")






