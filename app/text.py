# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 20:24:46 2024

@author: CEO1
"""

des_main = """
        The application provides a user-friendly interface for editing images, 
        allowing users to apply filters, resize images, adjust brightness/contrast, and more. 
        
        Here's a detailed overview of its features and implementation:
        Features:
        
        Upload Image:
            Allow users to upload images from their local computer.
            Supported formats: JPEG, PNG, BMP, etc.
    
        Display Image:
            Display the uploaded image for preview and editing.    
    
        Resize Image:
            Change the dimensions of the image.
            Maintain aspect ratio option.
    
        Colour adjustment:
            Adjust the colour of the image using sliders.
    
        Cropping:
            Allow users to select a region of the image to crop.
    
        Image Rotation:
            Rotate the image by 90, 180, or 270 degrees.
    
        Download Edited Image:
            Provide an option to download the edited image.
            
        """
        
des_page2 = """
            An app that performs arithmetic operations on images can be designed to allow 
            users to combine images in various ways using mathematical operations such as 
            addition, subtraction, multiplication, and division. This can be useful for tasks 
            like blending images, enhancing certain features, or performing image masking. 
            Here's a detailed overview of such an app, which we can call "Image Arithmetic Lab
            """

add_code = """
        import cv2  
        import numpy as np  
            
        # path to input images are specified and   
        # images are loaded with imread command  
        image1 = cv2.imread('input1.jpg')  
        image2 = cv2.imread('input2.jpg') 
          
        # cv2.addWeighted is applied over the 
        # image inputs with applied parameters 
        weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0) 
          
        # the window showing output image 
        # with the weighted sum  
        cv2.imshow('Weighted Image', weightedSum) 
          
        # De-allocate any associated memory usage   
        if cv2.waitKey(0) & 0xff == 27:  
            cv2.destroyAllWindows()  """
            
subtract_code = """
            # Python program to illustrate 
            # arithmetic operation of 
            # subtraction of pixels of two images 
            
            # organizing imports 
            import cv2 
            import numpy as np 
            	
            # path to input images are specified and 
            # images are loaded with imread command 
            image1 = cv2.imread('input1.jpg') 
            image2 = cv2.imread('input2.jpg') 
            
            # cv2.subtract is applied over the 
            # image inputs with applied parameters 
            sub = cv2.subtract(image1, image2) 
            
            # the window showing output image 
            # with the subtracted image 
            cv2.imshow('Subtracted Image', sub) 
            
            # De-allocate any associated memory usage 
            if cv2.waitKey(0) & 0xff == 27: 
            	cv2.destroyAllWindows()
                """
                
edge_desc = """
            Edge detection is one of the fundamental image-processing tasks used 
            in various Computer Vision tasks to identify the boundary or 
            sharp changes in the pixel intensity. It plays a crucial role in object detection, 
            image segmentation and feature extraction from the image.
                  """

grey_desc = """
            Grayscaling is the process of converting an image from other color spaces 
            e.g. RGB, CMYK, HSV, etc. to shades of gray. It varies between complete 
            black and complete white.
            """
            
resize_desc = """
                Resizing images is a fundamental task in image processing and computer vision, 
                involving the alteration of an image's dimensions—its width and height. 
                This process is essential for various applications, such as preparing 
                images for machine learning models, optimizing website performance, adjusting 
                image sizes for display on different devices, and more.
              """






                

