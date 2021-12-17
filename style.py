import math
import pandas as pd
import requests
import streamlit as st
import time
import os

def shishikan():
    st.write(
        """
        <div class="base-wrapper">
            <span class="section-header primary-span">ONDA MORTES DIÁRIAS POR MUNICÍPIO</span>
            <br><br>
            <span class="ambassador-question"><b>Selecione seu estado e município para prosseguir</b></span>
        </div>""",
        unsafe_allow_html=True,
    )