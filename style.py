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
                    <div class="white-span header p1" style="font-size: 30px;"><img class="icon-cards" src="data:image/png;base64,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" alt="Fonte: Impulso">QUER SABER MAIS SOBRE A VACINAÇÃO?</div>
                    <span class="white-span">Acompanhe nossos novos dados e descobra como avança a vacinação no seu município ou estado!<br><br>
                    <a class="btn-ambassador" href="https://farolcovid.coronacidades.org/?page=Vacin%C3%B4metro" target="_self">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Veja aqui!&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>
                    <br><br><span class="white-span">Saiba quando podemos controlar a pandemia no Brasil no nosso estudo realizado com dados inéditos obtidos pela Lei de Acesso à Informação.<br><br>
                    <a class="btn-ambassador" href="https://farolcovid.coronacidades.org/?page=Estudo+Vacina%C3%A7%C3%A3o" target="_self">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ler aqui!&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>
    </span></span></div></div></div></div>
         """)