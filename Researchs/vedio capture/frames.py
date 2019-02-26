import cv2
vid = 'output.mp4'
vidcap = cv2.VideoCapture(vid)
success,image = vidcap.read()
count = 0
threshold = 150

while success:

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  score = cv2.Laplacian(image, cv2.CV_64F).var()
  print score
  if score > threshold:
        	print("Not Blur")
		cv2.imwrite("frame-"+vid+"-%d.jpg" % count, image)     # save frame as JPEG file
  else:
        	print "Blur"

  #cv2.imwrite("frame-"+vid+"-%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
