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

def get_textinfo(entry_var):
        button_info = entry_var.get()
        print(button_info)

#hexcodes for our color pallet:
def insert_entry(label_name, text, entry_var):
    # labels the textbox
    label_name = tk.Label(text = text, font = ('Century 12'), bg = grey, fg = white)
    label_name.pack()

    #actual textbox
    entry_var = tk.Entry()
    entry_var.pack()

    # button = tk.Button(window, command = get_textinfo(entry_var))
    # button.pack()
    #gets information from textbox

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

page_info = tk.Label(text = "Please enter your profile information\n We use this when you need help\n\n", font = ('Century 12'), bg = grey, fg = white)
page_info.pack()

username = 1
enter_username = 1
username_text = "Enter your first and last name"
insert_entry(username, username_text, enter_username)

age = 1
enter_age = 1
age_text = "How old are you?"
insert_entry(age, age_text, enter_age)

pronouns = 1
enter_pronouns = 1
pronouns_text = "What are your pronouns?"
insert_entry(username, pronouns_text, enter_pronouns)

info = 1
enter_info = 1
info_text = "Any other important information? (Hard of hearing? Best language to use?)"
insert_entry(info, info_text, enter_info)


#this is what keeps the window running
window.mainloop()
