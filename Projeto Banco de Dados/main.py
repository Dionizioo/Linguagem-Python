import tkinter as tk
from conn import ConexaoBanco
from menu import Menu

conn = ConexaoBanco()

root = tk.Tk()
root.title("Menu")
root.minsize(300, 300)
Menu(conn, root)

root.mainloop()

conn.close()