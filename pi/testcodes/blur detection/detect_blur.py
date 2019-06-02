import glob
import cv2

images = [cv2.imread(file) for file in glob.glob("*.jpg")]
threshold = 1000
print len(images)
#image = cv2.imread('frame-VID_20190212_170903.mp4-115.jpg')
for image in images:
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	score = cv2.Laplacian(image, cv2.CV_64F).var()
	print score
	if score > threshold:
        	print "Not Blur"
	else:
        	print "Blur"
