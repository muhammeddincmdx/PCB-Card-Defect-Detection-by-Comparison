import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance


def resize_image(image, max_width, max_height):
    height, width = image.shape[:2]
    scaling_factor = min(max_width / width, max_height / height)
    new_size = (int(width * scaling_factor), int(height * scaling_factor))
    return cv2.resize(image, new_size)

# Function to merge close contours


# Way1
#-------------------------------------------------------------------------------------------

def merge_close_contours(contours, min_distance=0, max_distance=50):
    if len(contours) == 0:
        return []

    merged_contours = []
    centers = [cv2.moments(cnt) for cnt in contours]
    centers = [(int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])) if M['m00'] != 0 else (0, 0) for M in centers]

    merged = [False] * len(contours)

    for i in range(len(contours)):
        if not merged[i]:
            current_merge = [contours[i]]
            for j in range(i + 1, len(contours)):
                if not merged[j]:
                    
                    distance = np.sqrt((centers[i][0] - centers[j][0])**2 + (centers[i][1] - centers[j][1])**2)
                    if min_distance <= distance <= max_distance:
                        current_merge.append(contours[j])
                        merged[j] = True
            merged_contours.append(np.concatenate(current_merge))
            merged[i] = True

    return merged_contours

"""
# Way2
#-------------------------------------------------------------------------------------------

def merge_close_contours(contours, min_distance=20, max_distance=70):
    if len(contours) == 0:
        return []

    merged_contours = []
    centers = [cv2.moments(cnt) for cnt in contours]
    centers = [(int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])) if M['m00'] != 0 else (0, 0) for M in centers]
    distances = distance.cdist(centers, centers, 'euclidean')
    
    merged = [False] * len(contours)
    
    for i in range(len(contours)):
        if not merged[i]:
            current_merge = [contours[i]]
            for j in range(i + 1, len(contours)):
                if not merged[j] and min_distance <= distances[i, j] <= max_distance:
                    current_merge.append(contours[j])
                    merged[j] = True
            merged_contours.append(np.concatenate(current_merge))
            merged[i] = True
            
    return merged_contours
"""


# Function to merge overlapping bounding rectangles
def merge_overlapping_rectangles(rectangles):
    if len(rectangles) == 0:
        return []

    rectangles = [list(rect) for rect in rectangles]
    merged_rectangles = []

    while rectangles:
        rect1 = rectangles.pop(0)
        to_merge = [rect1]

        for rect2 in rectangles:
            if (rect1[0] < rect2[0] + rect2[2] and rect1[0] + rect1[2] > rect2[0] and
                rect1[1] < rect2[1] + rect2[3] and rect1[1] + rect1[3] > rect2[1]):
                to_merge.append(rect2)

        for rect in to_merge:
            if rect in rectangles:
                rectangles.remove(rect)

        x_min = min([rect[0] for rect in to_merge])
        y_min = min([rect[1] for rect in to_merge])
        x_max = max([rect[0] + rect[2] for rect in to_merge])
        y_max = max([rect[1] + rect[3] for rect in to_merge])
        
        merged_rectangles.append((x_min, y_min, x_max - x_min, y_max - y_min))

    return merged_rectangles


imageA = cv2.imread('3.jpg')
imageB = cv2.imread('4.jpg')

# Check dimensions
h, w = imageA.shape[:2]
warp_matrix = np.eye(2, 3, dtype=np.float32)

# ECC algorithm for alignment
criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 5000, 1e-10)
(cc, warp_matrix) = cv2.findTransformECC(cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY), cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY), warp_matrix, cv2.MOTION_TRANSLATION, criteria)

# Align the second image
aligned_imageB = cv2.warpAffine(imageB, warp_matrix, (w, h), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)

# Resize images to fit the screen
max_width = 800  
max_height = 600  
imageA_resized = resize_image(imageA, max_width, max_height)
aligned_imageB_resized = resize_image(aligned_imageB, max_width, max_height)


average_image = cv2.addWeighted(imageA_resized, 0.5, aligned_imageB_resized, 0.5, 0)


diff = cv2.absdiff(imageA_resized, aligned_imageB_resized)

# Apply a specific threshold value for detecting color difference (can be change for different images!!)
_, thresh = cv2.threshold(cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY), 101, 255, cv2.THRESH_BINARY)


kernel = np.ones((5, 5), np.uint8)
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Merging close contours
merged_contours = merge_close_contours(contours)


edge_margin = 10  # to prevent edge contours


rectangles = []
for contour in merged_contours:
    if cv2.contourArea(contour) > 100 :  
        x, y, w, h = cv2.boundingRect(contour)
        if x > edge_margin and y > edge_margin and x + w < imageA_resized.shape[1] - edge_margin and y + h < imageA_resized.shape[0] - edge_margin:
            rectangles.append((x, y, w, h))


merged_rectangles = merge_overlapping_rectangles(rectangles)


for (x, y, w, h) in merged_rectangles:
    cv2.rectangle(imageA_resized, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.rectangle(aligned_imageB_resized, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.rectangle(average_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display images using matplotlib
plt.figure(figsize=(20, 10))

plt.subplot(1, 4, 1)
plt.title('Reference Image')
plt.imshow(cv2.cvtColor(imageA_resized, cv2.COLOR_BGR2RGB))

plt.subplot(1, 4, 2)
plt.title('Aligned Image')
plt.imshow(cv2.cvtColor(aligned_imageB_resized, cv2.COLOR_BGR2RGB))

plt.subplot(1, 4, 3)
plt.title('Average Image')
plt.imshow(cv2.cvtColor(average_image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 4, 4)
plt.title('Differences')
plt.imshow(thresh, cmap='gray')

plt.tight_layout()
plt.show()
