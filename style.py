import math
import pandas as pd
import requests
import streamlit as st
import time
import streamlit.components.v1 as components


def shishikan():
    st.write(
    f"""
    <div class="conteudo" id="navbar">
    <a>&nbsp;</a>
    <a href="{urlpath}?page=Inicio">Início</a>
    <a href="{urlpath}?page=Metodologia">Modelos, limitações e fontes</a>
    <a class="active" href="{urlpath}?page=Quem-Somos">Quem somos?</a>
    <a href="{urlpath}?page=Estudo-Vacinacao">Estudo Vacinação</a>
    <a href="{urlpath}?page=Vacinometro">Vacinômetro</a>
    </div>
    """,
    unsafe_allow_html=True,
    )
