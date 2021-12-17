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
    <a href="{https://farolcovid.coronacidades.org/}?page=Inicio">Início</a>
    <a href="{https://farolcovid.coronacidades.org/}?page=Metodologia">Modelos, limitações e fontes</a>
    <a class="active" href="{https://farolcovid.coronacidades.org/}?page=Quem-Somos">Quem somos?</a>
    <a href="{https://farolcovid.coronacidades.org/}?page=Estudo-Vacinacao">Estudo Vacinação</a>
    <a href="{https://farolcovid.coronacidades.org/}?page=Vacinometro">Vacinômetro</a>
    </div>
    """,
    unsafe_allow_html=True,
    )
