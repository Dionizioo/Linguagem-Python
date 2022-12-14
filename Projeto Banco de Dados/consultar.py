import tkinter as tk
import menu

class Consultar:
    def __init__(self, conn, master=None):
        self.master = master
        self.conn = conn
        
        self.fontePadrao = ("Arial", "10")
        self.body = tk.Frame(master)
        self.body["pady"] = 10
        self.body.pack()

        self.idContainer = tk.Frame(master)
        self.idContainer["padx"] = 20
        self.idContainer.pack()
        
        self.voltarContainer = tk.Frame(master)
        self.voltarContainer["pady"] = 20
        self.voltarContainer.pack()
        
        vsql="SELECT*FROM tb_contatos"
        res = self.consultar(self.conn, vsql)
        
        self.idLabel = tk.Text(self.idContainer, font=self.fontePadrao)
        
        for r in res:
            self.idLabel.insert(tk.INSERT, "Id: " + str(r[0]) + "   Nome: " + r[1] + "\n")
            
            
        self.idLabel.pack(side=tk.LEFT)

        
        self.voltar = tk.Button(self.voltarContainer)
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = ("Calibri", "8")
        self.voltar["width"] = 12
        self.voltar["command"] = self.back
        self.voltar.pack(side=tk.LEFT)
        
    def back(self):
        self.limpar()
        self.master.title("Menu")
        menu.Menu(self.conn, self.master)
        
    def consultar(self, conn, vsql):
        c=conn.cursor()
        c.execute(vsql)
        res=c.fetchall()
        return res
    
    def limpar(self):
        for widgets in self.body.winfo_children():
            widgets.destroy()
        self.body.destroy()
        for widgets in self.idContainer.winfo_children():
            widgets.destroy()
        self.idContainer.destroy()
        for widgets in self.voltarContainer.winfo_children():
            widgets.destroy()
        self.voltarContainer.destroy()