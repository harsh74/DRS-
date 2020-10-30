import tkinter
import cv2
import PIL.Image,PIL.ImageTk
import imutils
import time
from functools import partial
import thread
stream=cv2.VideoCapture("runout.mp4")
a=2
def play(speed):
    global a
    print("speed is",speed)
    fr1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,fr1+speed)
    grabbed,frame=stream.read()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0, 0, anchor=tkinter.NW, image=frame)
    if(a%2==0):
        canvas.create_text(200,20,font="Times 20 italic bold",text="D E C I S I O N  P E N D I N G")
    a=a+1
def pending(decision):

    frame= cv2.cvtColor(cv2.imread("aa.jpg"), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0, 0, anchor=tkinter.NW, image=frame)
    time.sleep(1)
    if(decision=="out"):
        frame = cv2.cvtColor(cv2.imread("out.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, anchor=tkinter.NW, image=frame)
    else:
        frame = cv2.cvtColor(cv2.imread("Untitled.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, anchor=tkinter.NW, image=frame)

def out():

    thread=threading.Thread(target=pending,args=("out",))
    thread.deamon=1
    thread.start()
    print("out")

def notout():


    thread=threading.Thread(target=pending,args=("notout",))
    thread.deamon=1
    thread.start()
    print(" not out")

SET_WIDTH=700
SET_HEIGHT=400

root =tkinter.Tk()
root.configure(bg="black")
cv_img = cv2.cvtColor(cv2.imread("c.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(root, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()
btn1 = tkinter.Button(root, text="<<PREVIOUS FAST", bd=10, width=50, command=partial(play, -25))
btn1.pack()
btn2 = tkinter.Button(root, text="<<PREVIOUS SLOW", bd=10, width=50, command=partial(play, -4))
btn2.pack()
btn3 = tkinter.Button(root, text="NEXT FAST>>", bd=10, width=50, command=partial(play, 25))
btn3.pack()
btn4 = tkinter.Button(root, text="NEXT SLOW>>", bd=10, width=50, command=partial(play, 2))
btn4.pack()
btn5 = tkinter.Button(root, text="OUT", bd=10, width=50, command=out)
btn5.pack()
btn6 = tkinter.Button(root, text="NOT OUT", bd=10, width=50, command=notout)
btn6.pack()
root.mainloop()


