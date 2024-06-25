# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:30:37 2024

@author: CEO1
"""

import streamlit as st
import numpy as np
from PIL import Image
from text import edge_desc, grey_desc, resize_desc
import cv2 
import io

def downloading(new_image):
    img_pil = Image.fromarray(new_image)
    img_byte_arr = io.BytesIO()
    img_pil.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    return img_byte_arr
   

def resizing(image, new_height, new_width):
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    return resized_image

  
def canny_edge_detection(image):
    
    sub_image = Image.open(image).convert('RGB')
    frame = np.array(sub_image)
    # Convert the frame to grayscale for edge detection 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
      
    # Apply Gaussian blur to reduce noise and smoothen edges 
    blurred = cv2.GaussianBlur(src=gray, ksize=(3, 5), sigmaX=0.5) 
      
    # Perform Canny edge detection 
    edges = cv2.Canny(blurred, 70, 135) 
      
    st.image(edges, use_column_width =True)
    return edges

def grayscale(image):
    sub_image = Image.open(image).convert('RGB')
    frame = np.array(sub_image)
     
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    st.image(gray_scale, use_column_width = True)    
    return gray_scale
    

st.subheader("Resizing Image")
st.text(resize_desc)
uploadedfile2 = st.file_uploader("Upload an Image", type=['jpg', 'png', 'jpeg'])
if uploadedfile2 != None:
   image = Image.open(uploadedfile2)
   image = np.array(image)
    
    # Display the original image
   st.image(image, caption='Original Image', use_column_width=True)

    # Get new dimensions from the user
   new_width = st.number_input("New Height", min_value=1, step =10,value=500)
   new_height = st.number_input("New Width", min_value=1,step = 10,  value=500)
   
   
   if st.button("Resize Image"):
        # Resize the image
       resized_image = resizing(image, new_width, new_height)

        # Display the resized image
       st.image(resized_image, caption='Resized Image', use_column_width=False)
       img1 = downloading(resized_image)
       
       st.download_button(label="Download Resized Image", data=img1, file_name='resized_image.jpg', mime='image/jpeg')
      

st.divider()

st.subheader("Grayscale Transformation")
st.text(grey_desc)
uploadedfile3 = st.file_uploader("Upload an Image.", type = ["jpg", "png", "jpeg"])
if uploadedfile3 != None:
    st.image(uploadedfile3)
    st.markdown("#")
    st.markdown("***GRAYSCALED IMAGE***")
    gray = grayscale(uploadedfile3)
    img2 = downloading(gray)
    
    st.download_button(label="Download Grayscaled Image", data=img2, file_name='grayscaled_image.jpg', mime='image/jpeg')
    

st.divider()
st.subheader("Edge detection")
st.text(edge_desc)
uploadedfile4 = st.file_uploader("Upload an image", type = ["jpg", "png", "jpeg"])
if uploadedfile4 != None:
    st.image(uploadedfile4)
    st.markdown("#")
    st.markdown("***Output Image***")
    canny = canny_edge_detection(uploadedfile4)
    img3 = downloading(canny)
    
    st.download_button(label="Download Edited Image", data=img3, file_name='edited_image.jpg', mime='image/jpeg')
    

st.divider()
if st.button("Next Page"):
    st.switch_page("pages/page_4.py")
    
    
    
    
    
     
    
    
    
    
    
    
    
    
    
    
    