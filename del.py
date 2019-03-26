"""
from tkinter import *
import time
root = Tk()

text = Text(root)

for i in range(5):

    text.insert(INSERT, "Hello, world!\n"+str(i))
    text.pack(expand=1, fill=BOTH)

    # adding a tag to a part of text specifying the indices
    text.tag_add("makeRed", "1.8", "1.13")
    text.tag_config("makeRed", background="white", foreground="red")
    root.after(1000)
    text.delete('1.0', END)
    root.mainloop()
"""


from tkinter import *

def blink():
    for i in range(5):
        text.insert("1.0", "Hello, world!" + str(i)+"\\r")
        # expand=1, fill=BOTH)

        # adding a tag to a part of text specifying the indices
        text.tag_add("makeRed", "1.8", "1.13")
        text.tag_config("makeRed", background="white", foreground="red")
        #text.after(1000)
        text.delete('1.0', END)
        #root.after(100, lambda: text.config(bg='white')) # after 1000ms



root = Tk()
text = Text(root)
text.pack()
b = Button(root, text="Button", command=blink)
b.pack()
#e = Entry(root)
#e.pack()
root.mainloop()
