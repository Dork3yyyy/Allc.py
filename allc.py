#Allc GUI Desktop app

#root1

from tkinter import *
import pyglet, os
import webbrowser
from pytube import YouTube
from tkinter import messagebox as ms
import requests
import pyautogui
from PIL import Image
import pyqrcode 
import png 
from pyqrcode import QRCode

#functarea


def takescreen():
    def takescreenn():
        pic= pyautogui.screenshot()
        pic.save('image1.png')
    
    root4 = Tk()
    root4.title("Allc")
    root4.geometry("200x200")

    pyglet.font.add_file('NeueMachina-Regular.otf') 

    b1 = Button(root4, text="Take", command=takescreenn,fg="#fff", bg="#c0392b", activebackground="#e74c3c",font=('NeueMachina-Regular',12,)).place(relx=0.5, rely=0.5, anchor=CENTER)

    root4.resizable(False, False) #unresizeable
    root4.configure(bg='#34495e')
    root4.mainloop()

def qrroot():
    def generatee():
        s = inpute.get()
        url = pyqrcode.create(s) 
        url.png('myqr.png', scale = 6) 

    root5 = Tk()
    root5.title("Allc")
    root5.geometry("375x667")

    pyglet.font.add_file('NeueMachina-Regular.otf') 

    inpute = Entry(root5,fg="#fff", bg="#c0392b")
    inpute.place(y=280,x=125)

    b2 = Button(root5, text="Generate", command=generatee,fg="#fff", bg="#c0392b", activebackground="#e74c3c",font=('NeueMachina-Regular',12,)).place(relx=0.5, rely=0.5, anchor=CENTER)

    root5.resizable(False, False) #unresizeable
    root5.configure(bg='#34495e')
    root5.mainloop()

def callback(urll):
    webbrowser.open_new(urll,entry.pack())

def down():
    def click():
        yt = YouTube(inpute.get())
        stream = yt.streams.first()
        stream.download()
    
    root2 = Tk()
    root2.title("Allc")
    root2.geometry("375x667")

    pyglet.font.add_file('NeueMachina-Regular.otf') 

    inpute = Entry(root2,fg="#fff", bg="#c0392b")
    inpute.place(y=280,x=125)

    b1 = Button(root2, text="Download", command=click,fg="#fff", bg="#c0392b", activebackground="#e74c3c",font=('NeueMachina-Regular',12,)).place(relx=0.5, rely=0.5, anchor=CENTER)

    root2.resizable(False, False) #unresizeable
    root2.configure(bg='#34495e')
    root2.mainloop()

def imagedown():
    def click():
        url = inpute.get()
        path = "Image.jpg"
        r = requests.get(url)
        with open(path,"wb") as file:
            file.write(r.content)
    
    root3 = Tk()
    root3.title("Allc")
    root3.geometry("375x667")

    pyglet.font.add_file('NeueMachina-Regular.otf') 

    inpute = Entry(root3,fg="#fff", bg="#c0392b")
    inpute.place(y=280,x=125)

    b1 = Button(root3, text="Download", command=click,fg="#fff", bg="#c0392b", activebackground="#e74c3c",font=('NeueMachina-Regular',12,)).place(relx=0.5, rely=0.5, anchor=CENTER)

    root3.resizable(False, False) #unresizeable
    root3.configure(bg='#34495e')
    root3.mainloop()

pyglet.font.add_file('NeueMachina-Regular.otf') 

root1 = Tk()
root1.title("Allc")
root1.geometry("375x667")

#icon
  
p1 = PhotoImage(file = 'icon.png') 
root1.iconphoto(False, p1) 

#enterbutton

entbutton = Button(text="Youtube Download",fg="#fff", bg="#c0392b", activebackground="#e74c3c", padx=9,command=down, font=('NeueMachina-Regular',12,)).place(relx=0.5, rely=0.5, anchor=CENTER)
#entbutton.place(relx=0.5, rely=0.5, anchor=CENTER)
#btn = Button(text="Quit", command=root1.destroy).place(relx=0.5, rely=0.5, anchor=CENTER)

photobutton = Button(text="Image Download",fg="#fff", bg="#c0392b", activebackground="#e74c3c", padx=9, command=imagedown, font=('NeueMachina-Regular',12,)).place(y=270,x=105)
screenbutton = Button(text="Take Screenshot",fg="#fff", bg="#c0392b", activebackground="#e74c3c",command=takescreen, padx=9, font=('NeueMachina-Regular',12,)).place(y=225,x=107)

codegenrtor = Button(text="QR CODE",fg="#fff", bg="#c0392b", activebackground="#e74c3c",command=qrroot, padx=9, font=('NeueMachina-Regular',12,)).place(y=360,x=135)

#socialMedia

link1 = Label(root1, text="Social Media", fg="#c0392b",bg="#34495e", cursor="hand2",font=('NeueMachina-Regular',12,))
link1.pack(side=BOTTOM)
link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))

#speedtest

root1.resizable(False, False) #unresizeable
root1.configure(bg='#34495e')
root1.mainloop()