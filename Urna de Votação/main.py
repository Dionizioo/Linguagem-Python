import csv

import PySimpleGUI as gf
import matplotlib.pyplot as grafico

with open("Texto.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for linha in arquivo_csv:
        dados = []
        feminino = int(linha[1])
        masculino = int(linha[0])
        genero = 0
        n = 0
        norte = int(linha[2])
        nor = int(linha[3])
        co = int(linha[4])
        sud = int(linha[5])
        sul = int(linha[6])

        while True:
            layout = [
                [gf.Text("Informe seu Genero:")],
                [gf.Radio('Feminino','genero', key ='feminino'), gf.Radio('Masculino','genero', key='masculino')],
                [gf.Text('Informe sua Região:')],
                [gf.Radio('Norte','regiao', key='norte'), gf.Radio('Nordeste','regiao', key='nordeste'),gf.Radio('Centro-Oeste','regiao', key='co'),
                 gf.Radio("Sudeste",'regiao',key='sudeste'),gf.Radio("Sul",'regiao',key='sul')],
                [gf.Text("Informe o numero do seu candidato: ")],
                [gf.Radio('Lula', 'candidato',key='cand1'), gf.Radio('Jair Bolsonaro', 'candidato',key='cand2'),gf.Radio('Nulo', 'candidato',key='cand3')],
                [gf.Button("Confirmar")],
                [gf.Button("Grafico De Genero")],
                [gf.Button("Grafico De Região")],
                [gf.Button("Exit")]
            ]

            window = gf.Window("",layout)
            event,resp = window.read()
            window.close()

            if event == 'Confirmar':


                if resp['feminino']:

                    feminino += 1
                    genero = "F"
                    with open("Texto.csv", "w") as arquivo:
                        arquivo.write(
                            str(masculino) + "," + str(feminino) + "," + str(norte) + "," + str(nor) + "," + str(
                                co) + "," + str(sud) + "," + str(sul))

                else:
                    masculino += 1
                    genero = "M"
                    with open("Texto.csv", "w") as arquivo:
                        arquivo.write(
                            str(masculino) + "," + str(feminino) + "," + str(norte) + "," + str(nor) + "," + str(
                                co) + "," + str(sud) + "," + str(sul))

                #regiao = resp['regiao']

                if resp['norte'] == True:
                    regiao = "Norte"
                    #n += 1
                    norte +=1
                    with open("Texto.csv", "w") as arquivo:
                        arquivo.write(
                            str(masculino) + "," + str(feminino) + "," + str(norte) + "," + str(nor) + "," + str(
                                co) + "," + str(sud) + "," + str(sul))

                if resp['nordeste'] == True:
                    regiao = "nordeste"
                    #n += 1
                    nor +=1
                    with open("Texto.csv", "w") as arquivo:
                        arquivo.write(
                            str(masculino) + "," + str(feminino) + "," + str(norte) + "," + str(nor) + "," + str(
                                co) + "," + str(sud) + "," + str(sul))

                if resp['co'] == True:
                    regiao = "Centro-Oeste"
                    #n += 1
                    co +=1
                    with open("Texto.csv", "w") as arquivo:
                        arquivo.write(
                            str(masculino) + "," + str(feminino) + "," + str(norte) + "," + str(nor) + "," + str(
                                co) + "," + str(sud) + "," + str(sul))

                if resp['sudeste'] == True:
                    regiao = "Sudeste"
                    #n += 1
                    sud +=1
                    with open("Texto.csv", "w") as arquivo:
                        arquivo.write(
                            str(masculino) + "," + str(feminino) + "," + str(norte) + "," + str(nor) + "," + str(
                                co) + "," + str(sud) + "," + str(sul))

                if resp['sul'] == True:
                    regiao = "Sul"
                    #n += 1
                    sul +=1
                    with open("Texto.csv", "w") as arquivo:
                        arquivo.write(
                            str(masculino) + "," + str(feminino) + "," + str(norte) + "," + str(nor) + "," + str(
                                co) + "," + str(sud) + "," + str(sul))

                if resp['cand1'] == True:
                    candidato = 'Lula'
                elif resp['cand2'] == True:
                    candidato = 'Jair Bolsonaro'
                elif resp['cand3'] == True:
                    candidato = 'Nulo'

                dados=(regiao,genero,candidato)

            if event == "Grafico De Genero":

                '''feminino = 0
                masculino = 0
                i = 0
                for dado in dados:
                    if dado[i] == 'feminino':
                        feminino += 1
                    else:
                        masculino += 1'''

                x =["masculino","feminino"]
                y =[masculino,feminino]

                grafico.bar(x,y)
                grafico.show()

            if event == "Grafico De Região":

                x=["Norte","Nordeste","Centro-Oeste","Sudeste","Sul"]
                y=[norte,nor,co,sud,sul]

                grafico.bar(x, y)
                grafico.show()



            if event == 'Exit':
                with open("Texto.csv", "w") as arquivo:
                    arquivo.write(str(masculino) + "," + str(feminino) + "," + str(norte) + "," + str(nor) + "," + str(co) + "," + str(sud) + "," + str(sul))
                    break