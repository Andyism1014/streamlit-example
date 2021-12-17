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
    from flask import Flask
    from flask.templating import render_template

    app = Flask(__name__, static_url_path='/static')


    @app.route('/')
    def index():
        return render_template('index.html', name='home')


    if __name__ == "__main__":
        app.run(debug=True)
    def navigation():
        try:
            path = st.experimental_get_query_params()['p'][0]
        except Exception as e:
            st.error('Please use the main app.')
            return None
        return path
    if navigation() == "home":
        st.title('Home')
        st.write('This is the home page.')

    elif navigation() == "results":
        st.title('Results List')
        for item in range(25):
            st.write(f'Results {item}')

    elif navigation() == "analysis":
        st.title('Analysis')
        x, y = st.number_input('Input X'), st.number_input('Input Y')
        st.write('Result: ' + str(x+y))

    elif navigation() == "examples":
        st.title('Examples Menu')
        st.write('Select an example.')


    elif navigation() == "logs":
        st.title('View all of the logs')
        st.write('Here you may view all of the logs.')


    elif navigation() == "verify":
        st.title('Data verification is started...')
        st.write('Please stand by....')


    elif navigation() == "config":
        st.title('Configuration of the app.')
        st.write('Here you can configure the application')







