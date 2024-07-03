# 1. Method: Histogram Comparison
"""
Histogram comparison is a more primitive way of comparing two images. In this method,
you compare to color of the images.
For example, if you compare a red tomato and a green apple.
The similarity ratio will be low and close to %0.
It means they aren't similar.
But if you compare a red tomato with a red apple.
The similarity ratio will be high and close to %100.
It means similar. In fact, we know that tomatoes and red
apples aren't similar. The Histogram method compares two images
using color density. It is a basic, rapid method.

https://docs.opencv.org/3.4/d8/dbc/tutorial_histogram_calculation.html 


https://medium.com/@sasasulakshi/opencv-image-histogram-calculations-4c5e736f85e

"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

def compare_images(image1, image2,):
    
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    hist1 = cv2.calcHist([gray1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([gray2], [0], None, [256], [0, 256])
    
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    print(f"Similarity Ratio: {similarity * 100:.2f}%")
    
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.title('Image 1')
    plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
    
    plt.subplot(1, 2, 2)
    plt.title('Image 2')
    plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

    plt.show()


image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')
image3 = cv2.imread("fish1.jpg")
image4 = cv2.imread("fish2.jpg")
image5 = cv2.imread("j.jpeg")
image6 = cv2.imread("g.jpeg")

compare_images(image1, image2)
compare_images(image3, image4)
compare_images(image5, image6)