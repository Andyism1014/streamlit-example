import streamlit as st
import hydralit_components as hc
from Portfolio import *
from studio import *
from ETF import *
import streamlit_authenticator as stauth


st.set_page_config(page_title='Tensor Data Platform',  layout='wide')  # this needs to be the first Streamlit command

names = ['Tensorcorp']
usernames = ['tech@tensorcorp.com']
passwords = ['12345678']

hashed_passwords = stauth.hasher(passwords).generate()

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
    home_name='Home',
    hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)


if f"{menu_id}"=="Home":
    authenticator = stauth.authenticate(names,usernames,hashed_passwords,
        'some_cookie_name','some_signature_key',cookie_expiry_days=30)
    name, authentication_status = authenticator.login('Login','main')
    if st.session_state['authentication_status']:
        st.header('Welcome *%s*' % (name))
if f"{menu_id}"=="Portfolio":
    if st.session_state['authentication_status']:
        set_Portfolio()
if f"{menu_id}"=="Data Overview":
    if st.session_state['authentication_status']:
        dashbord2()
if f"{menu_id}"=="Studio":
    tabletry()
if f"{menu_id}"=="Beta":
    PerpOI()
if f"{menu_id}"=="Other":
    if st.session_state['authentication_status']:
        set_ETF()



    




    

    
