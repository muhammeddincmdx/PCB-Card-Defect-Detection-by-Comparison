# 4. Method Structural Similarity Index Measure
"""

SSIM is the method for finding similarity between two images.
This method is different from simple pixel by pixel methods. 
It consider luminance, contrast and structure when comparison. 
This  makes more accurate assessment of image comparison. 
The downsides of this method is more powerful tool for same 
scale images. And for the complex image it not perform good 
results. SSIM return a value around -1 and 1. 1 indicates 
images are so similar, and -1 incidates images are very different.

https://medium.com/srm-mic/all-about-structural-similarity-index-ssim-theory-code-in-pytorch-6551b455541e

"""

import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage.metrics import structural_similarity



def showdifference(img1,img2):
    # Convert to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Calculate Structural Similarity Index (SSIM)
    score, diff = structural_similarity(gray1, gray2, full=True)
    print("Similarity Score: {:.3f}%".format(score * 100))

    # Convert difference image to uint8
    diff = (diff * 255).astype("uint8")

    # Threshold the difference image
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # Find contours
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    # Create masks
    mask = np.zeros(img1.shape, dtype='uint8')
    filled = img2.copy()

    # Draw rectangles and contours
    for c in contours:
        area = cv2.contourArea(c)
        if area > 100:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img1, (x, y), (x + w, y + h), (36, 255, 12), 2)
            cv2.rectangle(img2, (x, y), (x + w, y + h), (36, 255, 12), 2)
            cv2.drawContours(mask, [c], 0, (0, 255, 0), -1)
            cv2.drawContours(filled, [c], 0, (0, 255, 0), -1)

    # Display images using matplotlib
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))

    # Original images
    axs[0, 0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    axs[0, 0].set_title('Image 1')
    axs[0, 0].axis('off')

    axs[0, 1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    axs[0, 1].set_title('Image 2')
    axs[0, 1].axis('off')

        # Difference image
    axs[0, 2].imshow(diff, cmap='gray')
    axs[0, 2].set_title('Difference')
    axs[0, 2].axis('off')

        # Mask
    axs[1, 0].imshow(mask)
    axs[1, 0].set_title('Mask')
    axs[1, 0].axis('off')

        # Filled image
    axs[1, 1].imshow(cv2.cvtColor(filled, cv2.COLOR_BGR2RGB))
    axs[1, 1].set_title('Filled Image 2')
    axs[1, 1].axis('off')

        # Show plot
    plt.tight_layout()
    plt.show()


image1 = cv2.imread("fish1.jpg")
image2 = cv2.imread("fish2.jpg")
image3 = cv2.imread("image1.jpg")
image4 = cv2.imread("image2.jpg")
image5 = cv2.imread("j.jpeg")
image6 = cv2.imread("g.jpeg")


showdifference(image1,image2)
showdifference(image3,image4)
showdifference(image5,image6)

