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

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark" >
<a class="navbar-brand" href="#">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAB1UExURQAAAAsLCw4ODioqKjY2NjU1NSsrK0REREVFRUNDQ0FBQUdHR0JCQkZGRjMzM0hISCwsLDk5OTc3NxkZGTQ0NB8fHycnJ3Z2dpaWlpOTk5SUlJKSknR0dJGRkbm5ubi4uLy8vLu7u76+vrq6ur29vXV1dQAAAKB6m0UAAAAndFJOU///////////////////////////////////////////////////AINWl9kAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGKSURBVHhe7dzBTsJAEIDhhgs3bg29EKPv/5ACGbAzJU3dbDXG75NwYNmd/vGkSTsAAAAAAAAAAAD/2mE4NLxi80z5wsZXbO7gFI7ffI/tT/cP17cs30/HsVfK4XRscioX0OucZkKEZEIqIUIyIZUQIZmQSoiQ7A+FrA9Y/IHWbOeQ1eOvix1/IxvE3LlNIbF9Va+Q6yXc/w2w6sVFLi7g5XfCyvmx+2dsCdkU+9uECNmJECE7ESJkJ0KEtDiMS7H00C1kw6xm4/ltqs7l9F4h4zkGzNRZzcbp/epj7n3aK2SKCQ/XyXVWs/FyC8n2C4kBM/1CNhwuREgDIUIyIZUQIZmQSoiQTEglREgmpBIiJBNSCRGSCamECMmEVEKEZEIqIUIyIZUQIZmQSoiQTEglREgmpBIiJBNSCRGSCamECMmEVEKEZP1CztMlmS7Lm8XGeNDEzOL5ivF5EksP95vFbgMePz1vFhviLroklp7iQRNJLH2Jz+di5SmOT2IJAAAAAAAAAADg7xqGT6c6KnWldvAfAAAAAElFTkSuQmCC" width="30" height="30" class="d-inline-block align-top" alt="">
Tensor Data Platform
</a>
</nav>
""", unsafe_allow_html=True)


#layout
if option=="Portfolio Information":
    set_Portfolio()
if option=="On-Chain Data":
    main()
if option=="Beta":
    st.write("gg")











