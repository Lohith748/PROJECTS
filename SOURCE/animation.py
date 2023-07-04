from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
root = Tk()
root.geometry("600x400")

def play_gif():
    global img
    img = Image.open("bin.gif")


    lbl = Label(root)
    lbl.place(x=0,y=0)

    for img in ImageSequence.Iterator(img):
        
        img = img.resize((300,300))
        img = ImageTk.PhotoImage(img)
        lbl.config(image= img)
        root.update()   
        time.sleep(0.01)
    root.after(0,play_gif)            
def exit():
    root.destroy()

    
    
Button(root,text = "play",command= play_gif).place(x=500,y=300)
Button(root,text = "exit",command= exit).place(x=450,y=300)




root.mainloop()
