from os import strerror, write
import pandas as pd
import streamlit as st
from PIL import Image
from Portfolio import *
from On_Chain import *
import time


im = Image.open("logo.png")
st.set_page_config(page_title='Tensor Data Platform',  layout='wide', page_icon=im)  # this needs to be the first Streamlit command

t1, t2 = st.columns((0.07,1))
t1.image('logo.png', width=100)
t2.title('Tensor Data Platform')
option = st.selectbox('Navigation',('Portfolio Information', 'On-Chain Data', 'Beta'))

#layout
if option=="Portfolio Information":
    set_Portfolio()
if option=="On-Chain Data":
    main()
if option=="Beta":
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
    st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #1d1f1d;">
    <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Tensor Data Platform</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
        <li class="nav-item active">
            <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">YouTube</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Twitter</a>
        </li>
        </ul>
    </div>
    </nav>
    """, unsafe_allow_html=True)












