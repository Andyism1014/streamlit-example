import altair as alt
import math
import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as components
import base64



def st_display_pdf(pdf_file):
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="800" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

def main():
    st.title("在Streamlit中嵌入PDF文件")
    st.subheader("Learn Streamlit")
    st_display_pdf("PDFembed.pdf")

