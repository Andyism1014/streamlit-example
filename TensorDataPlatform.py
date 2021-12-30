import streamlit as st
from PIL import Image
import hydralit_components as hc
from Portfolio import *
from studio import *
from ETF import *



im = Image.open("logo.png")
st.set_page_config(page_title='Tensor Data Platform',  layout='wide', page_icon=im)  # this needs to be the first Streamlit command

menu_data = [
    {'icon': "", 'label':"On-Chain Data"},
    {'icon': "", 'label':"Studio"},
    {'icon': "", 'label':"Beta"},
    {'icon': "", 'label':"Other"},
]

over_theme = {'txc_inactive': '#FFFFFF',"menu_background":"#3d3d3d"}

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)



if f"{menu_id}"=="Home":
    set_Portfolio()
if f"{menu_id}"=="On-Chain Data":
    dashbord2()
if f"{menu_id}"=="Studio":
    tabletry()
if f"{menu_id}"=="Other":
    set_ETF()
if f"{menu_id}"=="Beta":
    # Everything is accessible via the st.secrets dict:
    st.write("DB username:", st.secrets["db_username"])
    st.write("DB password:", st.secrets["db_password"])
    st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

    # And the root-level secrets are also accessible as environment variables:

    import os

    st.write(
        "Has environment variables been set:",
        os.environ["db_username"] == st.secrets["db_username"],
)


    




    

    
