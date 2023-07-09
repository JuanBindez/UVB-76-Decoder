import base64
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def help_info():
   """displays information about the program.
   clicking on the button will open a window with information.
   """
    
   window = Tk()
   window.title("UVB-76 Decoder")
   window.geometry("435x300")
   window.resizable(False, False)
   window.attributes('-alpha',9.1)

   custom_font_name = ('Arial', 15)
   label = Label(window,
                text="UVB-76 Decoder",
                font=custom_font_name).place(x=150, y=20)
   
   custom_font_version = ('Arial', 14)
   label = Label(window,
                text="v1.0.0",
                font=custom_font_version).place(x=188, y=58)


   label = Label(window,
                text="This software comes with absolutely no warranty.", ).place(x=45, y=154)

   label = Label(window, 
                text="For more details, visit the GNU General Public License, version 2", ).place(x=9, y=175)
                
   label = Label(window,
                text="Copyright © 2023  Juan Bindez",).place(x=120, y=260)