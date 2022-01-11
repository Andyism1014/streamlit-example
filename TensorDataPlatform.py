import streamlit as st
import hydralit_components as hc
from Portfolio import *
from studio import *



st.set_page_config(page_title='Tensor Data Platform',  layout='wide')  # this needs to be the first Streamlit command


menu_data = [
    {'icon': "", 'label':"Portfolio"},
    {'icon': "", 'label':"Data Overview"},
    {'icon': "", 'label':"Studio"},
    {'icon': "", 'label':"Beta"},
    {'icon': "", 'label':"Other"},
]

over_theme = {'txc_inactive': '#FFFFFF',"menu_background":"#3d3d3d"}

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    #home_name='Home',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)



if f"{menu_id}"=="Portfolio":
    set_Portfolio()
if f"{menu_id}"=="Data Overview":
    dashbord2()
if f"{menu_id}"=="Studio":
    tabletry()





    




    

    
