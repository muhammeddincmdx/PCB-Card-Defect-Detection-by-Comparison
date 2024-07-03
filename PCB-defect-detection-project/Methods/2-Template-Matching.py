# 2. Method: Template Matching
"""
Template matching is comparison method when finding a pattern
or an object. This method is need to a reference image
and template image from the reference image. There are
6 different method in the template mathcing. The downsides
of the this method are in the big images because of the calculation
it needs more calculation power and can be give some wrong results. 

"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

image1 = cv2.imread("try2.jpg")
template_img = cv2.imread("try1.jpg")


image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2RGB)


image2_copy = template_img.copy()


methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED',
           'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']


for m in methods:
    image1_copy = image1.copy()
    method = eval(m)  


    result = cv2.matchTemplate(image1_copy, template_img, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

 
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

   
    height, width, channels = template_img.shape
    bottom_right = (top_left[0] + width, top_left[1] + height)

   
    cv2.rectangle(image1_copy, top_left, bottom_right, (255, 0, 0), 10)


    fig = plt.figure(figsize=(10, 3))
    
    ax1 = fig.add_subplot(131)
    ax1.imshow(result, )
    ax1.set_title("Heatmap of Template Matching")

    ax2 = fig.add_subplot(132)
    ax2.imshow(image1_copy)
    ax2.set_title("Detection of Template")

    ax3 = fig.add_subplot(133)
    ax3.imshow(image2_copy)
    ax3.set_title("Template")
    
    fig.suptitle(m)
    plt.show()
    
    print("\n")
    print("\n")
