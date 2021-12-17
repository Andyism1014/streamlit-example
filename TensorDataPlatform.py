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
    import streamlit as st
    import hydralit_components as hc

    # specify the primary menu definition
    menu_data = [
            {'icon': "far fa-copy", 'label':"Left End"},
            {'id':'Copy','icon':"🐙",'label':"Copy"},
            {'icon': "far fa-chart-bar", 'label':"Chart"},#no tooltip message
            {'icon': "far fa-address-book", 'label':"Book"},
            {'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
            {'icon': "far fa-clone", 'label':"Component"},
            {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
            {'icon': "far fa-copy", 'label':"Right End"},
    ]
    # we can override any part of the primary colors of the menu
    #over_theme = {'txc_inactive': '#FFFFFF','menu_background':'red','txc_active':'yellow','option_active':'blue'}
    over_theme = {'txc_inactive': '#FFFFFF'}
    menu_id = hc.nav_bar(menu_definition=menu_data,home_name='Home',override_theme=over_theme)

        
    #get the id of the menu item clicked
    st.info(f"{menu_id=}")








