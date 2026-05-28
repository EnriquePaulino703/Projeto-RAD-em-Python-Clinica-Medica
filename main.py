#importando as bibliotecas necessárias
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk 
import sqlite3
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

# ---------------------------------------------------------
# 1. Função para limitar os caracteres do Entry
# ---------------------------------------------------------
def limitar_tamanho(*args):
    valor = cpf_var.get()
    # Se o texto digitado for maior que 11, corta o excedente
    if len(valor) > 11:
        cpf_var.set(valor[:11])

# ---------------------------------------------------------
# 2. Função para salvar no Banco de Dados (Simulando Login)
# ---------------------------------------------------------
def salvar_e_logar():
    cpf_digitado = cpf_var.get()
    
    # Validação simples para ver se tem exatamente 11 caracteres
    if len(cpf_digitado) == 11:
        # Conectando ao banco de dados SQLite
        conn = sqlite3.connect('banco_pedidos.db')
        cursor = conn.cursor()
        
        # Criando a tabela de usuários/sessão caso não exista
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessao_usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cpf TEXT UNIQUE
            )
        ''')
        
        try:
            # Tenta inserir o CPF novo
            cursor.execute("INSERT INTO sessao_usuario (cpf) VALUES (?)", (cpf_digitado,))
            conn.commit()
            
            # Atualiza o Label dentro do PDV com mensagem de SUCESSO (Verde)
            mensagem_label.config(text="CPF cadastrado com sucesso!, login realizado", fg="green")
            
        except sqlite3.IntegrityError:
            # Atualiza o Label dentro do PDV com mensagem de LOGIN (Azul)
            mensagem_label.config(text="CPF já cadastrado. Bem-vindo de volta!", fg="blue")
            
        conn.close()
        
        # AQUI VOCÊ CHAMA A PRÓXIMA TELA (A TELA DE PEDIDOS)
        # abrir_tela_de_pedidos(cpf_digitado)
        
    else:
        # Atualiza o Label dentro do PDV com mensagem de ERRO (Vermelho)
        mensagem_label.config(text="Atenção: O CPF precisa ter 11 dígitos.", fg="red")

# ---------------------------------------------------------
# 3. Interface e Vínculo das Variáveis
# ---------------------------------------------------------

# Variável de controle do Tkinter que será monitorada
cpf_var = StringVar()
cpf_var.trace_add("write", limitar_tamanho)

# Campo de Entry do CPF
cpf_entry = ttk.Entry(Downframe, textvariable=cpf_var, width=20, font=("Nunito", 20), justify="center")
cpf_entry.place(relx=0.5, y=110, anchor="n")

# --- NOVO: Label de Feedback visual integrado no PDV ---
# Inicia vazio (text="") e com fundo branco para combinar com o bg
mensagem_label = Label(Downframe, text="", font=("Nunito", 12, "bold"), bg="white")
mensagem_label.place(relx=0.5, y=160, anchor="n")

# Botão para disparar a ação de salvar (desci ele para o Y=200 para dar espaço à mensagem)
btn_entrar = ttk.Button(Downframe, text="CONFIRMAR", command=salvar_e_logar)
btn_entrar.place(relx=0.5, y=200, anchor="n")

janela_login.mainloop()