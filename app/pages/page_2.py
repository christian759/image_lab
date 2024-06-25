# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:23:09 2024

@author: CEO1
"""

import streamlit as st
import numpy as np
import cv2
from PIL import Image
import io
from text import add_code, subtract_code, des_page2


page_title = "Performing Arithmetic Operation on Images"
layout = "wide"

config = st.set_page_config(
        page_title=page_title,
        layout=layout,
        initial_sidebar_state="expanded",
)

st.header(page_title)


# Function to blend two images
def blend_images(image1, image2, alpha, beta, gamma):
    # Convert PIL images to numpy arrays
    image1_np = np.array(image1)
    image2_np = np.array(image2)

    # Resize images if they have different sizes
    if image1_np.shape[:2] != image2_np.shape[:2]:
        image2 = image2.resize(image1.size)

    # Convert resized image to numpy array
    image2_np = np.array(image2)

    # Check number of channels (RGB images should have 3 channels)
    if image1_np.shape[2] != 3 or image2_np.shape[2] != 3:
        raise ValueError("Input images must be RGB")

    # Blend images
    blended_image = cv2.addWeighted(image1_np, alpha, image2_np, beta, gamma)
    return blended_image


def subtract_image(image1, image2):
    image1_np = np.array(image1)
    image2_np = np.array(image2)

    # Resize images if they have different sizes
    if image1_np.shape[:2] != image2_np.shape[:2]:
        image2 = image2.resize(image1.size)

    # Convert resized image to numpy array
    image2_np = np.array(image2)

    # Check number of channels (RGB images should have 3 channels)
    if image1_np.shape[2] != 3 or image2_np.shape[2] != 3:
        raise ValueError("Input images must be RGB")
        
    subtracted_image = cv2.subtract(image1_np, image2_np)
    return subtracted_image


st.text(des_page2)
st.divider()
addition_des = "<h3> A simple Addition description </h3> "
st.markdown(addition_des, unsafe_allow_html = True)

uploaded_file1 = st.file_uploader("Upload Image 1", type=['jpg', 'png', 'jpeg'])
uploaded_file2 = st.file_uploader("Upload Image 2", type=['jpg', 'png', 'jpeg'])

if uploaded_file1 and uploaded_file2:
    # Convert uploaded files to PIL images
    image1 = Image.open(uploaded_file1).convert('RGB')
    image2 = Image.open(uploaded_file2).convert('RGB')

    # Display uploaded images
    st.image(image1, caption='Image 1', use_column_width=False)
    st.image(image2, caption='Image 2', use_column_width=False)

    # Slider for blending parameters
    alpha = st.slider('Image 1 weight', 0.0, 1.0, 0.5)
    beta = st.slider('Image 2 weight', 0.0, 1.0, 0.5)
    gamma = 0  # Setting gamma to 0 as per the original code

    # Button to blend images
    if st.button('Blend Images'):
        # Perform image blending
        try:
            blended_image = blend_images(image1, image2, alpha, beta, gamma)
            
            blended_image_rgb = cv2.cvtColor(blended_image, cv2.COLOR_BGR2RGB)

            # Display blended image
            st.subheader('Blended Image')
            st.image(blended_image_rgb, channels='BGR', use_column_width=False)
            
            img_pil = Image.fromarray(blended_image_rgb)
            img_byte_arr = io.BytesIO()
            img_pil.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            # Create download link
            st.download_button(label="Download Blended Image", data=img_byte_arr, file_name='blended_image.jpg', mime='image/jpeg')
        except ValueError as e:
            st.error(str(e))
            
st.markdown("##")
st.markdown("##")

subtraction_des = "<h3> A simple Subtraction description </h3> "
st.markdown(subtraction_des, unsafe_allow_html = True)

sub_uploaded_file1 = st.file_uploader("Upload Image1", type=['jpg', 'png', 'jpeg'])
sub_uploaded_file2 = st.file_uploader("Upload Image2", type=['jpg', 'png', 'jpeg'])

if sub_uploaded_file1 and sub_uploaded_file2:
    # Convert uploaded files to PIL images
    sub_image1 = Image.open(sub_uploaded_file1).convert('RGB')
    sub_image2 = Image.open(sub_uploaded_file2).convert('RGB')

    # Display uploaded images
    st.image(sub_image1, caption='Image 1', use_column_width=False)
    st.image(sub_image2, caption='Image 2', use_column_width=False)


    # Button to blend images
    if st.button('Subtract Image'):
        # Perform image blending
        try:
            sub_blended_image = subtract_image(sub_image1, sub_image2)
            
            sub_blended_image_rgb = cv2.cvtColor(sub_blended_image, cv2.COLOR_BGR2RGB)

            # Display blended image
            st.subheader('Subtract Image')
            st.image(sub_blended_image_rgb, channels='BGR', use_column_width=False)
            
            img_pil = Image.fromarray(sub_blended_image_rgb)
            img_byte_arr = io.BytesIO()
            img_pil.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            # Create download link
            st.download_button(label="Download Subtracted Image", data=img_byte_arr, file_name='subtracted_image.jpg', mime='image/jpeg')
        except ValueError as e:
            st.error(str(e))
            
st.divider()

with st.expander("Code Preview"):
    st.write("For the addition")
    st.code(add_code, language="python")
    st.markdown("##")
    st.write("For the subtraction")
    st.code(subtract_code, language="python")
        
        
        
if st.button("Next Page"):
    st.switch_page("pages/page_3.py")
        
        
        
        
        
    
  