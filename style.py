import streamlit as st
import streamlit.components.v1 as components

page_list = ['Portfolio Information', 'On-Chain Data', 'Beta']
query_params = st.experimental_get_query_params()
# Query parameters are returned as a list to support multiselect.
# Get the first item in the list if the query parameter exists.
default = int(query_params["option"][0]) if "option" in query_params else 0

option = st.sidebarradio("",page_list,index = default)
if option:
    query_params["option"] = page_list.index(option)
    st.experimental_set_query_params(**query_params)


if option=="Portfolio Information":
    set_Portfolio()
if option=="On-Chain Data":
    main()
