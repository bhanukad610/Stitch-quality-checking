import picamera     # Importing the library for camera module
from time import sleep  # Importing sleep from time library to add delay in program
import os


#function to create a folder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


import cv2
camera = picamera.PiCamera()    # Setting up the camera


def capture():
        vid = 'video14.h264'
        vidcap = cv2.VideoCapture(vid)
        success,image = vidcap.read()
        camera.start_preview()      # You will see a preview window while recording
        camera.start_recording('/home/pi/Project/System/testcodes/'+vid)
        sleep(7)
        camera.stop_recording()
        camera.stop_preview()

        
        # Release everything if job is finished
        #cap.release()
        #out.release()
        cv2.destroyAllWindows()



        #seperating and filter blued frames
        #vid = 'video1.h264'
        vidcap = cv2.VideoCapture(vid)
        success,image = vidcap.read()
        count = 0
        threshold = 10

        while success:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                score = cv2.Laplacian(image, cv2.CV_64F).var()
                print(score)
                if score > threshold:
                                print("Not Blur")
                                createFolder('./Images'+vid+'/')
                                path = 'Images'+vid
                                cv2.imwrite(os.path.join(path,"frame-"+vid+"-%d.jpg" % count), image)    # save frame as JPEG file
                else:
                                print("Blur")

                success,image = vidcap.read()
                print('Read a new frame: ', success)
                count += 1

capture()
