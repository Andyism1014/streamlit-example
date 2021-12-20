from os import strerror, write
import pandas as pd
import streamlit as st
from PIL import Image
from Portfolio import *
from On_Chain import *
import streamlit.components.v1 as components
import time



im = Image.open("logo.png")
st.set_page_config(page_title='Tensor Data Platform',  layout='wide', page_icon=im)  # this needs to be the first Streamlit command
st.markdown("""  
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark" >
<a class="navbar-brand" href="#">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAB1UExURQAAAENDQ7y8vENDQ7y8vENDQ0NDQ0VFRUdHR7q6ury8vL29vUFBQUJCQkNDQ0VFRUZGRkhISLi4uLm5ubq6ury8vL6+vkVFRUFBQUJCQkNDQ0REREVFRUZGRkdHR0hISLi4uLm5ubq6uru7u7y8vL29vb6+vpO8NMYAAAAYdFJOUwAqKjU1X5+fn5+fn8nJycnJycnJycnJ1GLIJUIAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKdSURBVHhe7dxtV5swGIDh0mJ968BZbAGLDpn9/z9x9OxBS56okKWN7e7r43DJbiDE7pwyAQAAAAAAAAAAAAAAAPA/i2ZOIvnrb3yN4yqap0krHSm5NP4F0eX4MXbzzn2VzNJHB5synckAYpaUGzk4ijmOs11IKYMOZwlJHULaiQkxuYU82kLk0AiEWLBGzjbE5fHrO2Q8TyGt73dFWCMywL9yC2Ef6Qsf8h1vrSRsSPLtQhz3EY8hZS7DjmALeSoqObqnKJ+K0vLnIi/9hSyqanyJJWSx0SGb5zIv8+LDK55X1cJXSHSVpF99SF3LvO9sIVWu7q31z/bz7N3dh5+k26mv/H1ol/8F+MSFLrHdWrl55tcXMsAnvHUMsXtEGywhVSHH3pg/E5wOsdxaP8rCvLVOMyQp1fP3NEPSjdqPTvSKbM7mihByNDrE9ms8IcfDGiHkQE4jZBorUznU8RYyYC5n09tV9rBcZvuujdF9hUyvZYK/lsuHbHXrqyS+r3/Vv/uyWA4KHeL2+I0zmaDTTn1vzOUszppt89J3uBCZoNNObc7lLF4127rp+zrE7dZqT1pfvW1W/q7IS1PLCeocLkQm6NSNmstZe5bqVzlBnaNdkdfa461lDt46WkjrbEKWXBGDW4jr41cm2EOIyS2Exa4QYiKEkL7AIewjSuAQ1ohCiIkQQvoCh7CPKIFDWCMKISZCCOkLHMI+ogQOYY0ohJgIIaQvcAj7iBI4hDWiEGIihJC+wCHsI0rgENaIQoiJEEL6AoewjyiBQ1gjCiEmQgjpCxzCPqIEDmGNKN5Cpjfy1a09N8YXuKK5vGzineU9jfodGOY7GIfM5W7IV+osL7hQL50Y8jOH/PoeAAAAAAAAAAAAAAAAAAQzmfwBINWrkHv3C28AAAAASUVORK5CYII=" width="30" height="30" class="d-inline-block align-top" alt="">
Tensor Data Platform
</a>
</div>
</nav>
""",unsafe_allow_html=True)



radio_list = ['Portfolio Information', 'On-Chain Data', 'Beta']

page = st.selectbox(
    "",
    radio_list,
)


if page=="Portfolio Information":
    set_Portfolio()
    
if page=="On-Chain Data":
    main()
if page=="beta":



    




