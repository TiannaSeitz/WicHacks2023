#This file is the user interface for the bracelet owner
import tkinter as tk
from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image

grey = '#393841'
white = '#e8e9ea'
purple = '#504887'
pink = 'ad2775'
blue = '#5d8aa6'

window = tk.Tk(className= " TELL personal safety ")
window.geometry("800x400")
window['background'] = grey

logo = PhotoImage(file = "images\logo.png")
window.iconphoto(False, logo)

# logo_open = Image.open('images\logo.png')
# logo_open = logo_open.resize((100,100))
# label = tk.Label(image = logo_open)
# label.image = ImageTk.PhotoImage(logo_open)
#this is the text on the main window

name = tk.Label(text = "Welcome to TELL", font = ('CordiaUPC 16'), bg = grey, fg = blue)
name.pack()

tagline = tk.Label(text = "discrete personal safety communication\n\n", font = ('Century 12'), bg = grey, fg = blue)
tagline.pack()

#this is what keeps the window running
window.mainloop()
