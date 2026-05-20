#importando as bibliotecas necessárias
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk 
import re

#criando a primeira janela "Login"
janela_login = Tk()
janela_login.title("Bem vindo(a) à Clínica Legal")
janela_login.geometry("600x800")
janela_login.resizable(width=FALSE, height=FALSE)
janela_login.configure(background="White")


#-----controle das imagens e config---

#importando as imagens para logo
img_original = Image.open("Assets/Logo/main_logo.png")

#aqui utilizei a função de resize da biblioteca Pillow para mudar o tamanho da foto para
#padrão 600 x 300

img_resize = img_original.resize((600, 300), Image.Resampling.LANCZOS)
logo = ImageTk.PhotoImage(img_resize)


#-----criando a janela de login-------

#frame superior onde ficará a logo
Upframe = Frame(janela_login, width=600, height=300, relief=FLAT)
Upframe.pack(side=TOP)

logo_label = Label(Upframe, image=logo, bg="white")
logo_label.place(x=0, y=0, relwidth=1, relheight=1)

#frame inferior onde ficará o formulário de login
Downframe = Frame(janela_login, width=600, height=500, relief=FLAT)
Downframe.pack(side=BOTTOM, fill=X)


#--criando os textos do frame inferior

#texto de bem vindo
welcome_label= Label(Downframe, text= "Seja bem vindo(a)", font= ("Nunito", 26), 
                     bg="white", fg="black")
welcome_label.place(x=0, y=10, relwidth=1)

#texto do login
cpf_label= Label(Downframe, text="Digite seu CPF:", font= ("Nunito", 20), 
                 bg="white", fg="black")
cpf_label.place(x=0, y=60, relwidth=1)

#cpf_entry = ttk.Entry(Downframe, width=20, font=("Nunito", 20), justify="center")
#cpf_entry.place(relx=0.5, y=110, anchor="n")



janela_login.mainloop()