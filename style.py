import math
import pandas as pd
import requests
import streamlit as st
import time
import os

def shishikan():
        st.write(
        """
    <div class="base-wrapper flex flex-column" style="background-color:#F02C2E">
        <div class="white-span header p1" style="font-size:30px;">
        Acre está a 5 dias em crescimento da média móvel de mortes.<br>
        O pico de mortes até agora foi de 432 mortes  em 03/08/2020.
        </div>
    </div>
    <div class="base-wrapper flex flex-column" style="background-color:#0090A7">
        <div class="white-span header p1" style="font-size:30px;">
        Seu município está a 10 dias em queda da média móvel de mortes.<br>
        Seu pico de mortes foi de 53 mortes em 25/06/2020.
        </div>
    </div>""",
        unsafe_allow_html=True,
    )
