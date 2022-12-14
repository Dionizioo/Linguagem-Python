import tkinter as tk
import menu
from conn import query

class Deletar:
    def __init__(self, conn, master=None):
        
        self.master = master
        self.conn = conn
        
        self.master.minsize(300, 100)
        
        self.fontePadrao = ("Arial", "10")
        self.body = tk.Frame(master)
        self.body["pady"] = 10
        self.body.pack()

        self.idContainer = tk.Frame(master)
        self.idContainer["padx"] = 20
        self.idContainer["pady"] = 5
        self.idContainer.pack()
        
        self.confirmContainer = tk.Frame(master)
        self.confirmContainer["pady"] = 20
        self.confirmContainer.pack()

        self.idLabel = tk.Label(self.idContainer,text="Id: ", font=self.fontePadrao)
        self.idLabel.pack(side=tk.LEFT)

        self.id = tk.Entry(self.idContainer)
        self.id["width"] = 30
        self.id["font"] = self.fontePadrao
        self.id.pack(side=tk.RIGHT)
        
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
        vid = self.id.get()
        
        vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO="+vid
        vsql1="DELETE FROM tb_lugar WHERE N_IDCONTATO="+vid
        vsql2="DELETE FROM tb_sexo WHERE N_IDCONTATO="+vid
        query(self.conn,vsql)
        query(self.conn,vsql1)
        query(self.conn,vsql2)
        
        self.back()
    
    def clearWindow(self):
        for widgets in self.body.winfo_children():
            widgets.destroy()
        self.body.destroy()
        for widgets in self.idContainer.winfo_children():
            widgets.destroy()
        self.idContainer.destroy()
        for widgets in self.confirmContainer.winfo_children():
            widgets.destroy()
        self.confirmContainer.destroy()