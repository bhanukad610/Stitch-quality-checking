import RPi.GPIO as GPIO

def start(channel):
	print("hello")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.add_event_detect(10, GPIO.RISING, callback = start)

message = input("Press\n\n")
GPIO.cleanup()
