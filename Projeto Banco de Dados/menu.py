import tkinter as tk
from consultar import Consultar
from deletar import Deletar
from inserir import Inserir
from atualizar import Atualizar

class Menu:
    def __init__(self, conn, master=None):
        
        self.master = master
        self.conn = conn
        
        self.fontePadrao = ("Arial", "10")
        self.body = tk.Frame(master)
        self.body["pady"] = 20
        self.body.pack()

        self.menuContainer = tk.Frame(master)
        self.menuContainer["padx"] = 50
        self.menuContainer["pady"] = 80
        self.menuContainer.pack()
        
        self.inserir = tk.Button(self.menuContainer)
        self.inserir["text"] = "Inserir Novo Registro"
        self.inserir["font"] = ("Calibri", "8")
        self.inserir["width"] = 20
        self.inserir["pady"] = 10
        self.inserir["command"] = self.inserirRegistro
        self.inserir.pack()
        
        self.deletar = tk.Button(self.menuContainer)
        self.deletar["text"] = "Deletar"
        self.deletar["font"] = ("Calibri", "8")
        self.deletar["width"] = 20
        self.deletar["pady"] = 10
        self.deletar["command"] = self.deletarRegistro
        self.deletar.pack()
        
        self.atualizar = tk.Button(self.menuContainer)
        self.atualizar["text"] = "Atualizar"
        self.atualizar["font"] = ("Calibri", "8")
        self.atualizar["width"] = 20
        self.atualizar["pady"] = 10
        self.atualizar["command"] = self.atualizarRegistro
        self.atualizar.pack()

        self.consultar = tk.Button(self.menuContainer)
        self.consultar["text"] = "Lista"
        self.consultar["font"] = ("Calibri", "8")
        self.consultar["width"] = 20
        self.consultar["pady"] = 10
        self.consultar["command"] = self.consultarRegistro
        self.consultar.pack()
        
    def consultarRegistro(self):
        self.limpar()
        self.master.title("inserir")
        Consultar(self.conn, self.master)
    
    def inserirRegistro(self):
        self.limpar()
        self.master.title("consultar")
        Inserir(self.conn, self.master)
    
    def deletarRegistro(self):
        self.limpar()
        self.master.title("deletar")
        Deletar(self.conn, self.master)
    
    def atualizarRegistro(self):
        self.limpar()
        self.master.title("atualizar")
        Atualizar(self.conn, self.master)
    
    def limpar(self):
        for widgets in self.body.winfo_children():
            widgets.destroy()
        self.body.destroy()
        for widgets in self.menuContainer.winfo_children():
            widgets.destroy()
        self.menuContainer.destroy()