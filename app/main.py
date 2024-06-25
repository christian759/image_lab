# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:30:10 2024

@author: CEO1
"""

import streamlit as st
from text import des_main


page_title = "Image Lab"
layout = "wide"

config = st.set_page_config(
        page_title=page_title,
        layout=layout,
        initial_sidebar_state="expanded",
)


description = ":blue[Image Lab: An Image Editing Application]"

st.title(page_title)
st.markdown(description)
st.text(des_main)
st.markdown("###")

if st.button("Next Page"):
    st.switch_page("pages/page_2.py")





