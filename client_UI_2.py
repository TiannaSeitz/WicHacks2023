import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import Image
import TEST

gray = '#393841'
white = '#e8e9ea'
light_pink = '#c09da7'
pink = '#ad2276'
blue = '#5d8aa6'

def get_name(name):
    username_label = tk.Label(text = ("Name: " + name), font = ('Century 16'), bg = gray, fg = white)
    username_label.pack(anchor='w')

def get_age(age):
    age_label = tk.Label(text = ("Age: " + age), font = ('Century 16'), bg = gray, fg = white)
    age_label.pack(anchor='w')

def get_pronouns(pronouns):
    pronouns_label = tk.Label(text = ("Pronouns: " + pronouns), font = ('Century 16'), bg = gray, fg = white)
    pronouns_label.pack(anchor='w')

def get_info(info):
    info_label = tk.Label(text = ("Additional info: " +  info), font = ('Century 16'), bg = gray, fg = white)
    info_label.pack(anchor='w')

def signal_type(signal):
    frame = Frame(win, highlightbackground = blue, bg = pink, highlightthickness = 4)
    frame.pack(padx = 20, pady = 20)
    info_label = tk.Label(frame, text = ("Signal: " +  signal), font = ('Century 20'), bg = light_pink, fg = pink)
    info_label.pack(anchor='w')

win = tk.Tk(className = " TELL Safety ")
win.geometry("800x500")
win['background'] = gray

logo = PhotoImage(file = "images\logo.png")
win.iconphoto(False, logo)

name = tk.Label(text = "Welcome to TELL", font = ('CordiaUPC 16'), bg = gray, fg = blue)
name.pack()

tagline = tk.Label(text = "Empowering you to take control of your safety\n\n", font = ('Century 12'), bg = gray, fg = blue)
tagline.pack()


name = "Apple Seed"
age = "21"
pronouns = "She/her"
info = "Hard of hearing"

signal_var = 2

if signal_var == 1:
    signal_in = "Escort me to my car"
elif signal_var == 2:
    signal_in = "Call a cab"
elif signal_var == 3:
    signal_in = "Call the police"

img_frame = Frame(win, highlightbackground = blue, bg = pink, highlightthickness = 4)
img_frame.pack(anchor = 'w')

profile_img = ImageTk.PhotoImage(Image.open("images\profile.jpg"))
profile_label = Label(img_frame, image = profile_img, height=90, width = 90)
profile_label.pack(anchor = 'w')


get_name(name)
get_age(age)
get_pronouns(pronouns)
get_info(info)
signal_type(signal_in)

win.mainloop()