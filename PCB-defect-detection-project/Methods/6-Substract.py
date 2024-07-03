import matplotlib.pyplot as plt
import numpy as np
import cv2



img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")
img3 = cv2.imread("5.jpg")
img4 = cv2.imread("6.jpg")
img5 = cv2.imread("fish1.jpg")
img6 = cv2.imread("fish2.jpg")


def SubtractMethod(imageA, imageB):
    
    imageA_resized = cv2.resize(imageA, (500, 500))
    imageB_resized = cv2.resize(imageB, (500, 500))

  
    grayA = cv2.cvtColor(imageA_resized, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB_resized, cv2.COLOR_BGR2GRAY)


    subtracted_gray = cv2.subtract(grayA, grayB)

   
    subtracted_bgr = cv2.cvtColor(subtracted_gray, cv2.COLOR_GRAY2BGR)


    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(imageA_resized, cv2.COLOR_BGR2RGB))
    plt.title('Image 1')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(imageB_resized, cv2.COLOR_BGR2RGB))
    plt.title('Image 2')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(subtracted_bgr, cv2.COLOR_BGR2RGB))
    plt.title('Difference')
    plt.axis('off')

    plt.show()



SubtractMethod(img4,img3)
SubtractMethod(img1,img2)
SubtractMethod(img5,img6)
