# 5. Method Absolute Diffrence

"""

Absolute Difference method is a pixel wise comparison method. 
Absolute difference thinking image as a matrix and taking 
difference between two matrix.

https://mesutpiskin.com/blog/opencv-arka-plan-temizleme-absdiff.html

https://stackoverflow.com/questions/65150972/difference-between-absdiff-and-normal-subtraction-in-opencv

"""


import cv2
import matplotlib.pyplot as plt


def AbsoluteDiff(imagea,imageb):

    difference = cv2.absdiff(imagea, imageb)



    
    image1_rgb = cv2.cvtColor(imagea, cv2.COLOR_BGR2RGB)
    image2_rgb = cv2.cvtColor(imageb, cv2.COLOR_BGR2RGB)
    difference_rgb = cv2.cvtColor(difference, cv2.COLOR_BGR2RGB)


    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(image1_rgb)
    plt.title('Image 1')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(image2_rgb)
    plt.title('Image 2')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(difference_rgb)
    plt.title('Difference')
    plt.axis('off')

    plt.show()


image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')
image3 = cv2.imread('fish1.jpg')
image4 = cv2.imread('fish2.jpg')
image5 = cv2.imread('5.jpg')
image6 = cv2.imread('6.jpg')

AbsoluteDiff(image1,image2)
AbsoluteDiff(image3,image4)
AbsoluteDiff(image5,image6)
