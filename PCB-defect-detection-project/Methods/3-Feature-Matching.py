# 3. Method Feature Matching
"""
Feature matching is another way for matching images.
This methods find keypoint and define descriptor
for this point and compare other image for
finding corresponding point. This method can find
different scale, size, or skewed image. There are
more than three way for feature matching. I only
show three of them.

https://stackoverflow.com/questions/11541154/checking-images-for-similarity-with-opencv

"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

""""
References
skp = sift keypoint
sdes = sift descriptor

sbf = sift brute force

"""



def display(img, title):
    
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    ax.set_title(title)
    plt.show()



img1 = cv2.imread('7.jpg',cv2.COLOR_BGR2GRAY)
img2 = cv2.imread("8.jpg",cv2.COLOR_BGR2GRAY)

# Method 1
#-------------------------------------------------------------------------------
orb = cv2.ORB_create()
kp1,des1 = orb.detectAndCompute(img1,None)
kp2,des2 = orb.detectAndCompute(img2,None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches = bf.match(des1,des2)
matches = sorted(matches,key= lambda x:x.distance )
matches = cv2.drawMatches(img1,kp1,img2,kp2,matches[:25],None,flags =2)

# Method 2
#-------------------------------------------------------------------------------
sift = cv2.SIFT_create()
skp1,sdes1 = sift.detectAndCompute(img1,None)
skp2,sdes2 = sift.detectAndCompute(img2,None)
sbf = cv2.BFMatcher()
sift_matches = sbf.knnMatch(sdes1,sdes2,k=2)

# less distance == better match
#ratio test
good_sift_matches = []
for match1,match2 in sift_matches:
   if match1.distance<0.75*match2.distance:
      good_sift_matches.append([match1])   
sift_matches = cv2.drawMatchesKnn(img1,skp1,img2,skp2,good_sift_matches[:25],None,flags=2)

# Method 3
#-------------------------------------------------------------------------------

sift = cv2.SIFT_create()
fkp1,fdes1 = sift.detectAndCompute(img1,None)
fkp2,fdes2 = sift.detectAndCompute(img2,None)
FLANN_INDEX_KDTREE=0
index_params = dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
search_params = dict(checks=50) 
flann = cv2.FlannBasedMatcher(indexParams=index_params,searchParams=search_params)
flann_matches= flann.knnMatch(fdes1,fdes2,k=2)



good_flann_matches = []
for fmatch1,fmatch2 in flann_matches:
   if fmatch1.distance>0.7*fmatch2.distance:
      good_flann_matches.append([fmatch2])

flann_matches=cv2.drawMatchesKnn(img1,fkp1,img2,fkp2,good_flann_matches[:25],None,flags=2)

display(matches,"OSB Method")
display(sift_matches,"SINF Method")
display(flann_matches,"FLANN Method")

