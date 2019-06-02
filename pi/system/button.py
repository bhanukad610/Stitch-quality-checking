from beep import alert
alert(0) #to indicate pi is bootup and starting to setup the system
alert(5)
from capture import capture
from predections import create_model
from predections import predict
import RPi.GPIO as GPIO
from sendToServer import sendToServer


user = "machine123" #this is identical to each machine

def start():
    capture()
    result = predict()
    numOfFrames = result[0]
    if numOfFrames == 0:
        print("fine")
    else:
        print("Number of frames : ", numOfFrames)
        sendToServer(user, str(numOfFrames))
        alert(4)
    #except ZeroDivisionError:
	#print("no images")

alert(1)
print("creating the model..")   
create_model()
print("model created")
alert(2)
print("system is ready")
alert(3)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


while True:
	if GPIO.input(10) == GPIO.HIGH:
	    try:
	      start()
	    except ZeroDivisionError:
	      print("images not found")
	      alert(6)

message = input("Press\n\n")
#GPIO.cleanup()
