import streamlit as st
import hydralit_components as hc
from Portfolio import *
from studio import *



st.set_page_config(page_title='Tensor Data Platform',  layout='wide')  # this needs to be the first Streamlit command


menu_data = [
    {'icon': "far fa-copy", 'label':"Portfolio"},
    {'icon': "far fa-chart-bar", 'label':"Data Overview", 'submenu':[{'id':'市场交易结构分析','icon': "fa fa-database", 'label':"市场交易结构分析"},{'id':'资金流与趋势分析','icon': "fa fa-database", 'label':"资金流与趋势分析"},{'id':'币安衍生品数据','icon': "fa fa-database", 'label':"币安衍生品数据"},{'id':'UTXO Realized Price Distribution (URPD)','icon': "fa fa-database", 'label':"UTXO Realized Price Distribution (URPD)"}]},
    {'icon': "", 'label':"Other"}
]

over_theme = {'txc_inactive': '#FFFFFF',"menu_background":"#3d3d3d"}

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='Sticky', #jumpy or not-jumpy, but sticky or pinned
)


if menu_id=="Portfolio":
    set_Portfolio()
if menu_id=="市场交易结构分析":
    st.subheader("市场交易活跃度与交易量")
    fenlei(aboutmarket[0:3])
    st.subheader("交易所余额")
    fenlei(aboutmarket[3:11])
    st.subheader("BTC 长期持有者")
    fenlei(aboutmarket[-3:])
if menu_id=="币安衍生品数据":
    longshortRatio()
if menu_id=="资金流与趋势分析":
    st.subheader("衍生品期货合约")
    fenlei(aboutderiva[0:8])
    st.subheader("稳定币")
    fenlei(aboutderiva[-3:])
if menu_id=="UTXO Realized Price Distribution (URPD)":
    st.write("UTXO Realized Price Distribution (URPD)")
    URPD()
#if f"{menu_id}"=="Studio":
    #tabletry()






    




    

    
