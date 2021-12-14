from os import strerror, write
import pandas as pd
import streamlit as st
from PIL import Image
from ETF import *
from Portfolio import *
import time
from macro import *

im = Image.open("logo.png")
st.set_page_config(page_title='Tensor Data Platform',  layout='wide', page_icon=im)  # this needs to be the first Streamlit command
t1, t2 = st.columns((0.12,1))
t1.image('logo.png', width=155)
t2.title('Tensor Data Platform')
t2.markdown("Tensor Investment Corporation | Proprietary trading and alternative investment firm")
option = st.selectbox('Navigation',('Portfolio Information', 'On-Chain Data', 'Beta'))

#layout
if option=="Portfolio Information":
    set_Portfolio()
if option=="On-Chain Data":
    set_ETF()
if option=="Beta":
    a=[]
    txt = st.text_area('Text to analyze', '''
    ss
     ''')
    if st.button('Start'):
        a.append(txt)
    st.write(a)






