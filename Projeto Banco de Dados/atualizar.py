import tkinter as tk
import menu
from atualizarForm import AtualizarForm

class Atualizar:
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
        self.idContainer["padx"] = 5
        self.idContainer.pack()
        
        self.confirmContainer = tk.Frame(master)
        self.confirmContainer["pady"] = 20
        self.confirmContainer.pack()

        self.idLabel = tk.Label(self.idContainer,text="Id", font=self.fontePadrao)
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
        menu.Menu(self.db, self.master)
    
    def confirm(self):
        vid = self.id.get()
        
        r=self.consultar(self.conn,"SELECT * FROM tb_contatos WHERE N_IDCONTATO="+vid)
        
        self.clearWindow()
        AtualizarForm(vid,r[0][1], r[0][2], r[0][3], r[0][1], r[0][1], self.conn, self.master)
        
    def consultar(self, conexao, sql):
        c=conexao.cursor()
        c.execute(sql)
        res=c.fetchall()
        return res
    
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