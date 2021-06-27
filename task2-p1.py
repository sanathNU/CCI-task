# NOT WORKING!!!

# program to find the real time dimensions of an object
from scipy.spatial import distance as dist
from imutils import perspective,contours
import imutils
import numpy as np 
import cv2

def midpoint(ptA,ptB):
    return  (ptA[0]+ptB[0])*0.5 , (ptA[1]+ptB[1])*0.5


img = cv2.imread('detect.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(7,7),0)

#performing edge detection by canary
edged = cv2.Canny(blurred,50,100)
dilated = cv2.dilate(edged,None,iterations=1)
eroded = cv2.erode(dilated,None,iterations=1)

#cv2.imshow("after preprocessing",eroded)
#cv2.waitKey(0)
#finding contours in the edge map
contour = cv2.findContours(eroded.copy(),
                          cv2.RETR_EXTERNAL,
                          CV2.CHAIN_APPROX_SIMPLE)
contour = imutils.grab_contours(contour)

#sorting the controus from left to right and initializing

(contour,_) = contours.sort_contours(contour)
pixelsPerMetric= None

#running a continous loop
for c in contour:
    #if the contour is not large enough, ignore it
    if cv2.contourArea(c) <100:
        continue
    
    #computing the rotated bouding box of the contour
    orig = imag.copy()
    box = cv2.minAreaRect(c)
    points = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(points,dtype='int')
    box = perspective.order_points(box)
    
    cv2.drawContours(orig,[box.astype("int")],-1,(0,255,0),2)
    # loop over the original points and draw them 
    for (x, y) in box: cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1
    
	# unpack the ordered bounding box, then compute the midpoint
	# between the top-left and top-right coordinates, followed by
	# the midpoint between bottom-left and bottom-right coordinates
	(tl, tr, br, bl) = box
	(tltrX, tltrY) = midpoint(tl, tr)
	(blbrX, blbrY) = midpoint(bl, br)
	# compute the midpoint between the top-left and top-right points,
	# followed by the midpoint between the top-righ and bottom-right
	(tlblX, tlblY) = midpoint(tl, bl)
	(trbrX, trbrY) = midpoint(tr, br)
	# draw the midpoints on the image
	cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
	cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
	cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
	cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
	# draw lines between the midpoints
	cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
		(255, 0, 255), 2)
	cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
		(255, 0, 255), 2)
    
    #compute the Euclidean distace between midpoings
    dA = dist.euclidean((tltrX,tltrY),(blbrX,blbrY))
    dB = dist.euclidean((tlblX,tltlY),(trbrX,trbrY))
    
    
    if pixelsPerMetric is None:
        pixelsPerMetric =dB/float(5.6)
        
    #computing the size of the object
    dimA = dA/ pixelsPerMetric
    dimB = dB/ pixelsPerMetric
    
    #draw the object sizes on the image
    cv2.putText(orig,"{:1f}in".format(dimA),
                (int(tlrX ~15),int(tlrY~10),cv2.FONT_HERSHEY_SIMPLEX,
                 0.65,(0,0,0),2)
                
    #showing the output image
    cv2.imshow("Image",orig)
    cv2.waitKey(0)
