import math
import pandas as pd
import requests
import streamlit as st
import time
import streamlit.components.v1 as components
import os

def shishikan():
    """ 
    This is a function that returns the "Footer" session 
    
    """
    if os.getenv("IS_HEROKU") == "TRUE":
        urlpath = os.getenv("urlpath")
    elif os.getenv("IS_DEV") == "TRUE":
        urlpath = 'http://localhost:8501/'
    else:
        urlpath = 'https://farolcovid.coronacidades.org/'

    st.write(
        f"""
        <div class="conteudo" id="navbar">
        <a>&nbsp;</a>
        <a href="{urlpath}?page=Inicio">Início</a>
        <a class="active" href="{urlpath}?page=Metodologia">Modelos, limitações e fontes</a>
        <a href="{urlpath}?page=Quem-Somos">Quem somos?</a>
        <a href="{urlpath}?page=Estudo-Vacinacao">Estudo Vacinação</a>
        <a href="{urlpath}?page=Vacinometro">Vacinômetro</a>
        </div>
        """,
    unsafe_allow_html=True,
    )