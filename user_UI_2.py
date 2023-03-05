import tkinter as tk
from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image

gray = '#393841'
white = '#e8e9ea'
purple = '#504887'
pink = 'ad2775'
blue = '#5d8aa6'

global name_var
global age_var

def get_name():
    name_var = username_entry.get()
    print(name_var)
    return name_var

def get_age():
    age_var = age_entry.get()
    print(age_var)
    return age_var

def get_pronouns():
    pronouns_var = pronouns_entry.get()
    print(pronouns_var)
    return pronouns_var

def get_info():
    info_var = info_entry.get()
    print(info_var)
    return info_var

def done(done_var):
    done_var = 1
    print(done_var)
    return done_var

win = tk.Tk(className = "TELL Safety")
win.geometry("1000x800")
win['background'] = gray

logo = PhotoImage(file = "images\logo.png")
win.iconphoto(False, logo)

username_label = tk.Label(text = "Tell us your name: ", font = ('Century 12'), bg = gray, fg = white)
username_label.pack()
username_entry = tk.Entry()
username_entry.pack()
username_button = Button(win, text = "Save", command = lambda: get_name())
username_button.pack()

age_label = tk.Label(text = "How old are you? ", font = ('Century 12'), bg = gray, fg = white)
age_label.pack()
age_entry = tk.Entry()
age_entry.pack()
age_button = Button(win, text = "Save", command = lambda: get_age())
age_button.pack()

pronouns_label = tk.Label(text = "What are your pronouns? ", font = ('Century 12'), bg = gray, fg = white)
pronouns_label.pack()
pronouns_entry = tk.Entry()
pronouns_entry.pack()
pronouns_button = Button(win, text = "Save", command = lambda: get_pronouns())
pronouns_button.pack()

info_label = tk.Label(text = "Anything else we should know? ", font = ('Century 12'), bg = gray, fg = white)
info_label.pack()
info_entry = tk.Entry()
info_entry.pack()
info_button = Button(win, text = "Save", command = lambda: get_info())
info_button.pack()

done_var = 0

done_button = Button(win, text = "Done", command = lambda: done(done_var))
done_button.pack()

win.mainloop()