
import os
import sqlite3
from sqlite3 import Error
import time


#conexaõ
def ConexaoBanco():
    caminho="agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con 

vcon=ConexaoBanco()

def query(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação Realizada com Sucesso")
        #conexao.close()
        
def consultar(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    res=c.fetchall()
    #conexao.close()
    return res
    

def menuPrincioal():
    print("1 - inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro")
    print("5 - Sair")

def menuInserir():
    vnome=input("Digite o Nome:")
    vtelefone=input("Digite o Telefone:")
    vemail=input("Digite o email:")
    vpais=input("Digite o pais:")
    vsexo=input("Digite o Sexo:")

    vsql="INSERT INTO tb_contatos (T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO) VALUES('"+vnome+"','"+vtelefone+"','"+vemail+"')"
    vsql1="INSERT INTO tb_lugar (T_PAIS) VALUES('"+vpais+"')"
    vsql2="INSERT INTO tb_sexo (T_SEXO) VALUES('"+vsexo+"')"
    
    query(vcon,vsql)
    query(vcon,vsql1)
    query(vcon,vsql2)
    

def deletar():
    vid=input("Digite o ID do Registro a ser Deletado: ")
    vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO="+vid
    vsql1="DELETE FROM tb_lugar WHERE N_IDCONTATO="+vid
    vsql2="DELETE FROM tb_sexo WHERE N_IDCONTATO="+vid
    query(vcon,vsql)
    query(vcon,vsql1)
    query(vcon,vsql2)

def atualizar():
    vid=input("Digite o ID do Registro a ser Alterado: ")
    r=consultar(vcon,"SELECT * FROM tb_contatos WHERE N_IDCONTATO="+vid)
    rnome=r[0][1]
    rtelefone=r[0][2]
    remail=r[0][3]
    rlugar=r[0][1]
    rsexo=r[0][1]
    vnome=input("Digite o Nome:")
    vtelefone=input("Digite o Telefone:")
    vemail=input("Digite o email:")
    vlugar=input("Digite o lugar: ")
    vsexo=input("Digite o sexo: ")
    if(len(vnome)==0):
        vnome=rnome
    if(len(vtelefone)==0):
        vtelefone=rtelefone
    if(len(vemail)==0):
        vemail=remail
    if(len(vlugar)==0):
        vlugar=rlugar
    if(len(vsexo)==0):
        vsexo=rsexo
    
    vsql="UPDATE tb_contatos SET T_NOMECONTATO='"+vnome+"',T_TELEFONECONTATO='"+vtelefone+"',T_EMAILCONTATO='"+vemail+"' WHERE N_IDCONTATO="+vid
    vsql1="UPDATE tb_lugar SET T_PAIS='"+vlugar+"' WHERE N_IDCONTATO="+vid
    vsql2="UPDATE tb_sexo SET T_SEXO='"+vsexo+"' WHERE N_IDCONTATO="+vid
    query(vcon,vsql)
    query(vcon,vsql1)
    query(vcon,vsql2)

def menuconsultar():
    vsql="SELECT*FROM tb_contatos"
    res=consultar(vcon,vsql)
    vlimi=10
    vcont=0
    for r in res:
        print("ID:{0} Nome:{1}".format(r[0],r[1]))
        if(vcont>=vlimi):
            vcont=0
            

    print("Fim da Lista")   
    
opc=0
while opc !=5:
    menuPrincioal()
    opc=int(input("Digite uma opção: "))
    if opc==1:
        menuInserir()
    elif opc==2: 
        deletar()
    elif opc==3: 
        atualizar()
    elif opc==4:  
        menuconsultar()
    elif opc==5:  
        print("Programa finalizado")
    else:
        print("opcao invalida")

vcon.close()






