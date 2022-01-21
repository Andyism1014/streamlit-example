import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from streamlit_autorefresh import st_autorefresh
import requests

st.set_page_config(page_title='Tensor DataBase Management', layout='wide')

engine = create_engine('sqlite:///database.db')

st.write("gg")
#%%
