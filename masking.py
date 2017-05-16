import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
def nothing(x):
    pass

camera = PiCamera()
camera.resolution = (360, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(360, 240))


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
	print image

#grayscale

	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#hue saturation value

	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)	

#defining the lower and the upper array

	lower_array = np.array([80, 96, 88])
	upper_array = np.array([109, 128, 117])

#masking between upper lower blue:

	mask = cv2.inRange(image, lower_array, upper_array)	

#result

	res = cv2.bitwise_and(image, image, mask= mask)

#define gaussian blur with edges & masking

	blur = cv2.GaussianBlur(mask, (5,5), 0)

#define threshholding for th1 & th2

        cv2.createTrackbar('th1','edges', 125, 255, nothing)
        cv2.createTrackbar('th2','edges', 125, 255, nothing)
        th1 = cv2.getTrackbarPos('th1','image')
        th2 = cv2.getTrackbarPos('th2','image')

#define the edge-detection for two threshholds

        edges = cv2.Canny(blur,th1,th2)

#define the blurring effects to edges

        k = np.ones((5,5), np.float32)/25
        s = cv2.filter2D(edges, -1, k)

#defineing the different frames


	cv2.imshow("Frame", image)
	cv2.imshow("gray",gray_image)
	cv2.imshow("hsv",hsv)
	cv2.imshow("mask",mask)
	cv2.imshow("res",res)
	cv2.imshow("edges",edges)
	cv2.imshow("blur",blur)
	key = cv2.waitKey(1) & 0xFF
 
	rawCapture.truncate(0)
 	if key == ord("q"):
		break
