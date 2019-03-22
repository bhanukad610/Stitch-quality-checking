import numpy as np
import cv2
import time
import os

cap = cv2.VideoCapture(0)

# The duration in seconds of the video captured
capture_duration = 3

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))

start_time = time.time()

while(int(time.time() - start_time) < capture_duration ):
    ret, frame = cap.read()
    if ret==True:
	gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
        cv2.imshow('frame',gray)
	frame = cv2.flip(frame,0,gray)

        # write the flipped frame
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

#function to create a folder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

#seperating and filter blued frames
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
                createFolder('./Images'+vid+'/')
                path = 'Images'+vid
                #cv2.imwrite(os.path.join(path , 'waka.jpg'), img)
		cv2.imwrite(os.path.join(path,"frame-"+vid+"-%d.jpg" % count), image)    # save frame as JPEG file
  else:
        	print "Blur"

  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

#delete the mp4 file
os.remove('output.mp4')
print("File Removed!")