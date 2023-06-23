# this is part of the UVB-76-Decoder project.
#
# Release: v1.0-rc7
#
# Copyright © 2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import os
import time
import datetime

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font

from src.decode_pt_module import *
from src.decode_us_module import *


window = Tk()
window.title("UVB-76 Decoder")
window.geometry("500x370")
#window['background'] = '#373636'  
window.resizable(False, False)# False for non-responsive window and True for responsive.
window.attributes('-alpha',9.1)
#foto_icon = PhotoImage(data=base64.b64decode(ICON_LOGO))
#window.iconphoto(True, foto_icon)


def decode_message():

    code = entrada_de_dados.get()
    numeros = [int(num) for num in code.split(",")]
    name_file = str(datetime.datetime.now())
    arquivo_saida = open("UVB-76-Decode-" + name_file + ".txt", "w")

    if var_portugues.get() == 1:
        for num in numeros:
            if num in message_text_pt:
                texto = message_text_pt[num]
                arquivo_saida.write(texto+"\n")

                print(message_text_pt[num])
            else:
                print("Número não possui um texto correspondente.")

    elif var_ingles.get() == 1:
        for num in numeros:
            if num in message_text_en:
                texto = message_text_en[num]
                arquivo_saida.write(texto+"\n")

                print(message_text_en[num])
            else:
                print("Número não possui um texto correspondente.")

    elif var_portugues.get() == 0 and var_ingles.get() == 0:
        print("marque idioma")


var_portugues = IntVar()
var_ingles = IntVar()

check_portugues = Checkbutton(window,
                         text="Portuguese",
                         bd=0,
                         variable=var_portugues,).place(x=80, y=220)

check_ingles = Checkbutton(window,
                        text="English",
                        bd=0,
                        variable=var_ingles).place(x=160, y=220)


def make_menu(w):
    global the_menu_1
    the_menu_1 = Menu(w, tearoff=0)
    the_menu_1.add_command(label="Colar")
    
    
def show_menu(e):
    w = e.widget
    the_menu_1.entryconfigure("Colar",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu_1.tk.call("tk_popup", the_menu_1, e.x_root, e.y_root)


make_menu(window)
entrada_de_dados = Entry(window, width=40)
entrada_de_dados.place(x=95, y=170)
entrada_de_dados.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
lbl = Label(window, text = "")

def funcao_opcao1():
    print("Opção 1 selecionada")

def funcao_opcao2():
    exit()


menu_barra = Menu(window)

menu_arquivo = Menu(menu_barra, tearoff=0)
menu_arquivo.add_command(label="Help", command=funcao_opcao1)
menu_arquivo.add_command(label="Quit", command=funcao_opcao2)

menu_barra.add_cascade(label="Menu", menu=menu_arquivo)
window.config(menu=menu_barra)


fonte_personalizada = font.Font(family="Times New Roman", size=24)
label = Label(window, text="UVB-76 Decoder", font=fonte_personalizada).place(x=150, y=100)

font_footer = font.Font(family="Times New Roman", size=12)
label = Label(window, text="1.0-rc7", font=font_footer).place(x=410, y=340)

font_decode = font.Font(family="Times New Roman", size=16)
botao_decode = Button(window,
                text="Decode",
                font=font_decode,
                command=decode_message,
                width=45,).place(x=2, y=300)


if __name__ == "__main__":
    window.mainloop()