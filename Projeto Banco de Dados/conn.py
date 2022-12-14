import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho="agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con 

def query(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
