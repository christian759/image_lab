# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:30:37 2024

@author: CEO1
"""

import streamlit as st
from text import edge_desc

import cv2 
  
def canny_edge_detection(frame): 
    # Convert the frame to grayscale for edge detection 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
      
    # Apply Gaussian blur to reduce noise and smoothen edges 
    blurred = cv2.GaussianBlur(src=gray, ksize=(3, 5), sigmaX=0.5) 
      
    # Perform Canny edge detection 
    edges = cv2.Canny(blurred, 70, 135) 
      
    return blurred, edges

st.subheader("Resizing Image")


st.subheader("color manipulation")



st.subheader("Grayscale Transformation")
st


st.subheader("Edge detection")
st.markdown(***edge_desc***)

if st.button("Next Page"):
    st.switch_page("pages/page_4.py")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    