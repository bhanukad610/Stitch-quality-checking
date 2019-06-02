from tkinter import *
root = Tk()
from capture import capture
from predections import create_model
from predections import predict
from sendToServer import sendToServer

create_model()

user = 'bhanuka'

def start():
    capture()
    label_result.config(text="Processing")
    result = predict()
    numOfFrames = result[0]
    if numOfFrames == 0:
        print("fine")
        label_result.config(text="fine")
    else:
        label_result.config(text=("Number of defects detected : ", numOfFrames))
        print("Number of defects detected : ", numOfFrames)
        sendToServer(user, str(numOfFrames))

top_frame = Frame(root)
top_frame.pack()

button = Button(top_frame, text = "Start", command = start)
label1 = Label(root, text = "Results :")
label_result = Label(root)

button.pack()
label1.pack()
label_result.pack()

root.mainloop()