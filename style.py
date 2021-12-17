import math
import pandas as pd
import requests
import streamlit as st
import time
import streamlit.components.v1 as components


def shishikan():
    components.html(
          """
    <div class="element-container" style="width: 1391px;"><div class="markdown-text-container stMarkdown" style="width: 1391px;"><div>
                <div class="base-wrapper flex flex-column" style="background-color: rgb(0, 144, 167);">
                    <div class="white-span header p1" style="font-size: 30px;">Tensor Data Platform</div>
                    <span class="white-span">Acompanhe nossos novos dados e descobra como avança a vacinação no seu município ou estado!<br><br>
                    <a class="btn-ambassador" href="https://farolcovid.coronacidades.org/?page=Vacin%C3%B4metro" target="_self">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Veja aqui!&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>
                    <br><br><span class="white-span">Saiba quando podemos controlar a pandemia no Brasil no nosso estudo realizado com dados inéditos obtidos pela Lei de Acesso à Informação.<br><br>
                    <a class="btn-ambassador" href="https://farolcovid.coronacidades.org/?page=Estudo+Vacina%C3%A7%C3%A3o" target="_self">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ler aqui!&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>
    </span></span></div></div></div></div>
         """)
