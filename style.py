import streamlit as st
import hydralit_components as hc


#make it look nice from the start
st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)

# specify the primary menu definition
menu_data = [
    {'icon': "far fa-copy", 'label':"Left End"},
    {'id':'Copy','icon':"🐙",'label':"Copy"},
]

over_theme = {'bgc_menu':'#FFFFFF',"menu_background":"#4c4c4c"}

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)



#get the id of the menu item clicked
st.write(f"{menu_id}") 