# IMPORT[pip install pillow]
from PIL import Image

# IMPORT [pip3 install customtkinter]
import customtkinter
from tkinter import messagebox, CENTER

class systemCRUD():
    def createUSER(self):
        regUSER = self.entry_regUsername.get()
        regPASS = self.entry_regPassword.get()
        regPASSCONFIRM = self.entry_regPasswordCONFIRM.get()
        regEMAIL = self.entry_regEmail.get()

        if regUSER == "":
            self.label_rules1.configure(text_color=self.color_warning)
        
        elif regPASS == "" or regPASSCONFIRM == "" or regPASS != regPASSCONFIRM:
            self.label_rules2.configure(text_color=self.color_warning)
        
        elif regEMAIL == "":
            self.label_rules3.configure(text_color=self.color_warning)

        else:
            lista = [regUSER, regPASS, regEMAIL]
            cur = self.connection.cursor()
            command = "INSERT INTO formulario (user, password, email) VALUES(?, ?, ?)"
            cur.execute(command, lista)

            messagebox.showinfo(
                title="Registro",
                message="Novo usuário criado com sucesso!"
            )

            # fechar banco de dados e janela de registro
            self.connection.close()
            self.registerROOT.destroy()
            

class LoginRegister(systemCRUD):
    def login(self):
        self.user = self.entry_username.get()
        self.password = self.entry_password.get()

        self.credencials = [
            ('admin', 'admin123'),
            ('baku-stark', 'baku123')
        ]

        if self.user == "" and self.password == "":
            messagebox.showerror(
                title="Login",
                message="Os campos precisam ser preenchidos"
            )

        elif self.user == "" or self.password == "":
            messagebox.showerror(
                title="Login",
                message="o campo de USUÁRIO/SENHA precisam ser preenchidos."
            )

        else:
            for login_item in self.credencials:

                if self.user == login_item[0] and self.password == login_item[1]:
                    messagebox.showinfo(
                        title=f"Bem-vindo, {self.user}",
                        message="O seu login foi efetuado com sucesso!"
                    )
                    break

                self.lista = [self.user, self.password]

            self.entry_username.delete(0, 'end')
            self.entry_password.delete(0, 'end')

    def framesMAIN(self):
        self.frameCENTER = customtkinter.CTkFrame(self.root)

        self.frameLEFT = customtkinter.CTkFrame(self.frameCENTER)

        self.img = customtkinter.CTkImage(dark_image=Image.open('img/ciberespaco.png'), light_image=Image.open('img/ciberespaco.png'), size=(130, 130))
        self.set_image = customtkinter.CTkLabel(
            self.frameLEFT, image=self.img, text="WELCOME", font=('Impact', 20), text_color=self.color_title
        )

        self.frameRIGHT = customtkinter.CTkFrame(self.frameCENTER)

        self.frameCENTER.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor=CENTER)
        self.set_image.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor=CENTER)
        self.frameLEFT.place(relwidth=0.5, relheight=1)
        self.frameRIGHT.place(relx=0.5, relwidth=0.5, relheight=1)

    def form_widgets(self):
        self.login_btn = customtkinter.CTkButton(
            self.frameRIGHT, text="LOGIN", font=('Impact', 15), fg_color="#111111", hover_color="#6E6E6E"
        )
        self.login_btn.configure(command=self.login)

        self.register_btn = customtkinter.CTkButton(
            self.frameRIGHT, text="REGISTRAR", font=('Impact', 15), fg_color="#485460", hover_color="#6E6E6E"
        )
        self.register_btn.configure(command=self.registerForm)

        self.label_username = customtkinter.CTkLabel(
            self.frameRIGHT, text="Usuário obrigatório*", font=('Arial', 15)
        )
        self.entry_username = customtkinter.CTkEntry(
            self.frameRIGHT, placeholder_text="Nome de usuário", placeholder_text_color="#56555e"
        )

        self.label_password = customtkinter.CTkLabel(
            self.frameRIGHT, text="Senha obrigatória*", font=('Arial', 15)
        )
        self.entry_password = customtkinter.CTkEntry(
            self.frameRIGHT, placeholder_text="Digite sua senha", placeholder_text_color="#56555e"
        )
        self.entry_password.configure(show="*")

        self.login_btn.place(relx=0.1, rely=0.6, relwidth=0.7)
        self.register_btn.place(relx=0.49, rely=0.7, relwidth=0.3)

        self.label_username.place(relx=0.01, rely=0.15)
        self.entry_username.place(relx=0.01, rely=0.25, relwidth=0.7)
        self.label_password.place(relx=0.01, rely=0.35)
        self.entry_password.place(relx=0.01, rely=0.45, relwidth=0.7)

    def registerForm(self):
        self.registerROOT = customtkinter.CTkToplevel()
        self.registerROOT.grab_set()
        self.registerROOT.focus_force()
        self.registerROOT.geometry("500x400")
        self.registerROOT.title("Registro de Usuário")
        self.registerROOT.iconbitmap('img/ciberespaco.ico')
        self.registerROOT.resizable(width='false', height='false')

        self.description = customtkinter.CTkLabel(
            self.registerROOT, text="Faça o registro de um novo usuário", text_color=self.color_letter,
            font=('Impact', 20), anchor='n'
        )

        self.label_rules1 = customtkinter.CTkLabel(
            self.registerROOT, text="Usuário OBRIGATÓRIO*", text_color="#56555e",
            font=('Arial', 15)
        )
        self.label_rules2 = customtkinter.CTkLabel(
            self.registerROOT, text="Senha OBRIGATÓRIA/IGUAIS*", text_color="#56555e",
            font=('Arial', 15)
        )
        self.label_rules3 = customtkinter.CTkLabel(
            self.registerROOT, text="E-mail OBRIGATÓRIO*", text_color="#56555e",
            font=('Arial', 15)
        )

        self.entry_regUsername = customtkinter.CTkEntry(
            self.registerROOT, placeholder_text="Registre um nome de usuário", placeholder_text_color="#56555e"
        )

        self.entry_regPassword = customtkinter.CTkEntry(
            self.registerROOT, placeholder_text="Senha", placeholder_text_color="#56555e"
        )
        self.entry_regPassword.configure(show="*")

        self.entry_regPasswordCONFIRM = customtkinter.CTkEntry(
            self.registerROOT, placeholder_text="Confirmar Senha", placeholder_text_color="#56555e"
        )
        self.entry_regPasswordCONFIRM.configure(show="*")

        self.entry_regEmail = customtkinter.CTkEntry(
            self.registerROOT, placeholder_text="Escolha um e-mail", placeholder_text_color="#56555e"
        )

        self.create_btn = customtkinter.CTkButton(
            self.registerROOT, text="Criar conta", font=('Impact', 15), fg_color="#111111", hover_color="#6E6E6E"
        )
        self.create_btn.configure(command=self.createUSER)

        self.description.place(relx=0.24, rely=0.05)

        self.label_rules1.place(relx=0.3, rely=0.12)
        self.label_rules2.place(relx=0.3, rely=0.22)
        self.label_rules3.place(relx=0.3, rely=0.32)

        self.entry_regUsername.place(relx=0.24, rely=0.4, relwidth=0.6)
        self.entry_regPassword.place(relx=0.24, rely=0.5, relwidth=0.6)
        self.entry_regPasswordCONFIRM.place(relx=0.24, rely=0.6, relwidth=0.6)
        self.entry_regEmail.place(relx=0.24, rely=0.7, relwidth=0.6)
        self.create_btn.place(relx=0.24, rely=0.8, relwidth=0.6)