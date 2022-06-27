#________________________________________
#ORGANIZAÇÃO INICIAL
import investpy as ip
import PySimpleGUI as sg
import tablepopup as ta

heading = ['data','open','high','low','close','volume','currency']
index = []
table = []
cont = 0

def busca_historic(stock, data_inicial, data_final, country, freq):
    if freq == True:
        result = ip.get_stock_historical_data(stock=stock, country=country,from_date=data_inicial, to_date=data_final, interval='Monthly')
    else:
        result = ip.get_stock_historical_data(stock=stock, country=country, from_date=data_inicial, to_date=data_final, interval='Daily')

    return [result.values.tolist(), result.index.tolist()]


#________________________________________
#DEFININDO LAYOUT
  #escolhendo o tema 
sg.theme('DarkBlack')
  #desenhando tela
layout_main = [
    [sg.Text('AÇÕES DATA', size=(50,2), justification='center')],

    [sg.Text('Cód Ativo '), sg.Input('',size=(34,5), key='_stock')], 

    [sg.Text('Data Inicio  '), sg.Input(key='_inicio',size=(10,3)), sg.Text('Data Fim  '), sg.Input(key='_fim', size=(10,3))],

    [sg.Text('Mensal'), sg.Checkbox('',key='_freq'), sg.Text('País'), sg.OptionMenu(['Brazil','United States','Japan','England','France','Germany','Canada'],s=(21,3),key='_country')],

    [sg.Button('Buscar')]
]
  #Janela_main
janela = sg.Window('Busca Ações', layout=layout_main)

#________________________________________
#LENDO TELA 
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Buscar':
        cont = 0
        table = []
        try:
            dados = busca_historic(values['_stock'],values["_inicio"],values["_fim"],values["_country"],values["_freq"])
            #adicionando indice
            for i in dados[0]:
                # print(dados[1][0])
                x = i
                x.insert(0,str(dados[1][cont])[:10])
                table.append(x)
                cont+=1
            
            if len(dados[1])<1:
                sg.popup('Erro no sistema, tente novamente')
            else:
                ta.table(table,heading,values['_inicio'],values['_fim'],values['_stock'])

            
        except:
            sg.popup_error('Digite as informações corretamente.')