import cv2

def doCanny(input, lowThresh, highThresh, aperture):
	if input.nChannels != 1:
		return(0)
	out = cv2.Create((input.width, input.height), input.depth, 1)
	cv2.Canny(input, out, lowThresh, highThresh, aperture)
	return out

def doPyrDown(input):
    assert(input.width !=0 and input.height !=0)
    out = cv2.Create((input.width/2, input.height/2), input.depth, input.nChannel)
    cv2.PyrDown(input, out)
    return out




img = cv2.CascadeClassifier("image.jpg")
img2 = cv2.CascadeClassifier((img.width, img.height), img.depth, 1)
cv2.cvtColor(img, img2, cv2.CV2_BGR2GRAY)
cv2.NamedWindow("Example Gray", cv2.CV2_WINDOW_AUTOSIZE)
cv2.Show("EXAMPLE GRAY", img2)
img3 = doCanny(img2, 10, 100, 3)



img2 = doPyrDown(img3)
cv2.Show("EXAMPLE 2", img2)
cv2.waitKey(0)
