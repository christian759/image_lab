import streamlit as st
import numpy as np
import cv2
from PIL import Image
import io


def downloading(new_image):
    img_pil = Image.fromarray(new_image)
    img_byte_arr = io.BytesIO()
    img_pil.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    return img_byte_arr


# Function to colorize an image
def colorize_image(image):
    # Convert PIL image to OpenCV format (BGR)
    img_rgb = np.array(image.convert("RGB"))
    img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

    # Create grayscale version
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Perform colorization (using OpenCV's cv2.applyColorMap for simplicity)
    img_colorized = cv2.applyColorMap(img_gray, cv2.COLORMAP_JET)

    return img_colorized

# Streamlit app

st.title("Simple Image Colorization App")
st.write("Upload a grayscale image and click 'Colorize' to see the result!")

uploaded_file = st.file_uploader("Choose a grayscale image...", type=["jpg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Grayscale Image', use_column_width=True)

    # Colorize image on button click
    if st.button('Colorize'):
        with st.spinner('Colorizing...'):
            # Perform colorization
            colorized_image = colorize_image(image)
            st.image(colorized_image, caption='Colorized Image', use_column_width=True)
            img4 = downloading(colorized_image)
            
            st.download_button(label="Download colorized image", data = img4, file_name = "colorized_image.jpg", mime = "image/jpeg")
            
