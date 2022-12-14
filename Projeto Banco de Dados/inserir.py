import tkinter as tk
import menu
from conn import query

class Inserir:
    def __init__(self, conn, master=None):
        
        self.master = master
        self.conn = conn
        
        self.master.minsize(300, 250)
        
        self.fontePadrao = ("Arial", "10")
        self.body = tk.Frame(master)
        self.body["pady"] = 10
        self.body.pack()

        self.nomeContainer = tk.Frame(master)
        self.nomeContainer["padx"] = 20
        self.nomeContainer["pady"] = 5
        self.nomeContainer.pack()
        
        self.telefoneContainer = tk.Frame(master)
        self.telefoneContainer["padx"] = 20
        self.telefoneContainer["pady"] = 5
        self.telefoneContainer.pack()
        
        self.emailContainer = tk.Frame(master)
        self.emailContainer["padx"] = 20
        self.emailContainer["pady"] = 5
        self.emailContainer.pack()
        
        self.paisContainer = tk.Frame(master)
        self.paisContainer["padx"] = 20
        self.paisContainer["pady"] = 5
        self.paisContainer.pack()
        
        self.sexoContainer = tk.Frame(master)
        self.sexoContainer["padx"] = 20
        self.sexoContainer["pady"] = 5
        self.sexoContainer.pack()
        
        self.confirmContainer = tk.Frame(master)
        self.confirmContainer["pady"] = 20
        self.confirmContainer.pack()

        self.nomeLabel = tk.Label(self.nomeContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=tk.LEFT)

        self.nome = tk.Entry(self.nomeContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=tk.RIGHT)
        
        self.telefoneLabel = tk.Label(self.telefoneContainer,text="Telefone", font=self.fontePadrao)
        self.telefoneLabel.pack(side=tk.LEFT)

        self.telefone = tk.Entry(self.telefoneContainer)
        self.telefone["width"] = 30
        self.telefone["font"] = self.fontePadrao
        self.telefone.pack(side=tk.RIGHT)
        
        self.emailLabel = tk.Label(self.emailContainer,text="E-mail", font=self.fontePadrao)
        self.emailLabel.pack(side=tk.LEFT)

        self.email = tk.Entry(self.emailContainer)
        self.email["width"] = 30
        self.email["font"] = self.fontePadrao
        self.email.pack(side=tk.RIGHT)
        
        self.paisLabel = tk.Label(self.paisContainer,text="Pais", font=self.fontePadrao)
        self.paisLabel.pack(side=tk.LEFT)
        
        self.pais = tk.Entry(self.paisContainer)
        self.pais["width"] = 30
        self.pais["font"] = self.fontePadrao
        self.pais.pack(side=tk.RIGHT)
        
        self.sexoLabel = tk.Label(self.sexoContainer,text="Sexo", font=self.fontePadrao)
        self.sexoLabel.pack(side=tk.LEFT)
        
        self.sexo = tk.Entry(self.sexoContainer)
        self.sexo["width"] = 30
        self.sexo["font"] = self.fontePadrao
        self.sexo.pack(side=tk.RIGHT)
        
        self.voltar = tk.Button(self.confirmContainer)
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = ("Calibri", "8")
        self.voltar["width"] = 12
        self.voltar["command"] = self.back
        self.voltar.pack(side=tk.LEFT)
        
        self.confirmar = tk.Button(self.confirmContainer)
        self.confirmar["text"] = "Confirmar"
        self.confirmar["font"] = ("Calibri", "8")
        self.confirmar["width"] = 12
        self.confirmar["command"] = self.confirm
        self.confirmar.pack(side=tk.RIGHT)
        
    def back(self):
        self.clearWindow()
        self.master.title("Menu")
        menu.Menu(self.conn, self.master)
    
    def confirm(self):
        vnome = self.nome.get()
        vtelefone = self.telefone.get()
        vemail = self.email.get()
        vpais = self.pais.get()
        vsexo = self.sexo.get()
        
        vsql="INSERT INTO tb_contatos (T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO) VALUES('"+vnome+"','"+vtelefone+"','"+vemail+"')"
        vsql1="INSERT INTO tb_lugar (T_PAIS) VALUES('"+vpais+"')"
        vsql2="INSERT INTO tb_sexo (T_SEXO) VALUES('"+vsexo+"')"
        
        query(self.conn,vsql)
        query(self.conn,vsql1)
        query(self.conn,vsql2)
        
        self.back()
    
    def clearWindow(self):
        for widgets in self.body.winfo_children():
            widgets.destroy()
        self.body.destroy()
        for widgets in self.nomeContainer.winfo_children():
            widgets.destroy()
        self.nomeContainer.destroy()
        for widgets in self.telefoneContainer.winfo_children():
            widgets.destroy()
        self.telefoneContainer.destroy()
        for widgets in self.emailContainer.winfo_children():
            widgets.destroy()
        self.emailContainer.destroy()
        for widgets in self.paisContainer.winfo_children():
            widgets.destroy()
        self.paisContainer.destroy()
        for widgets in self.sexoContainer.winfo_children():
            widgets.destroy()
        self.sexoContainer.destroy()
        for widgets in self.confirmContainer.winfo_children():
            widgets.destroy()
        self.confirmContainer.destroy()
