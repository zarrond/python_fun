from tkinter import *
import win32api

 
window = Tk()
 
window.title("My app")
 
window.geometry('350x200')
def clicked():
     
    lbl.configure(text="Button was clicked !!")
     
    btn = Button(window, text="Click Me", command=clicked)
     
    btn.grid(column=1, row=0)
while(1):
    x, y = win32api.GetCursorPos()
    lbl = Label(window, text="x:{} y:{}".format(x,y))
     
    lbl.grid(column=0, row=0)
     
    
    
    
    window.update()
window.mainloop()
    
