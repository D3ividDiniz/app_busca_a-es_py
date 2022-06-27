import PySimpleGUI as sg
from datetime import datetime
from openpyxl import Workbook
from time import sleep
conte = 0

# tabela = [sg.Table(values=C, headings=['open','high','low','close','volume','currency'] ,max_col_width=20,row_height=20,auto_size_columns=True, justification='center',key='tabela',num_rows=10),]
# # def (headings)


def table(dados, titulos,datai,dataf,stock):
    conti = 0
    table_layout = [
        [sg.Text(str('Resultados da ' + datai + '-' + dataf), justification='center'), sg.Button('Baixar Tabela')],
        [sg.Table(values=dados,headings=titulos,
        max_col_width=24,
        auto_size_columns=True,
        justification='right',
        row_height=30)]
    ]
    sleep(3)

    table_window = sg.Window('Resultados', table_layout, size=(500,400))

    while True:
        event, values = table_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Baixar Tabela':
            wb = Workbook()
            wb1 = wb.active
            for i in dados:
                print(i)
                conti+=1
                wb1['A'+str(conti)] = str(i)
            name = str(stock) + "_" + str(datetime.now()).replace(':','') + "_" + str(conte) + ".xlsx"
            wb.save(name)
            sg.popup_notify('Salvo com sucesso!')