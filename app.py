import PySimpleGUI as sg
from datetime import datetime

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Mês: ', size = (0, 5)),sg.Slider(range = (1, 12), default_value = 1, orientation = 'h', size = (45, 20), key = 'mês')],
            [sg.Text('Nome do Paciente: '), sg.Input(key = 'nome')],
            [sg.Text('Idade do Paciente: '), sg.Input(key = 'idade', size = (3, 2))],
            [sg.Text('Pagou ?')],
            [sg.Checkbox('Sim', key = 'sim'), sg.Checkbox('Não', key = 'nao')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size = (30, 20))]
            ]

        self.janela = sg.Window('Controle dos Pacientes').layout(layout)

    def iniciar(self):
        m2 = 0
        while True:
            self.button, self.value = self.janela.Read()

            nome = self.value['nome']
            idade = self.value['idade']
            pagou = self.value['sim']
            nao_pagou = self.value['nao']
            if pagou == True:
                pagou = 'PAGO'
            else:
                pagou = False
            if nao_pagou == True:
                pagou = 'NÃO-PAGO'
            mes = self.value['mês']
            for m in ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']:
                mes -= 1
                if mes == 0:
                    mes = m
                    break
            if m2 != mes:
                with open('Controle_Clientes.txt', 'a') as arquivo:
                    arquivo.write(('-='*35))
            m2 = mes
            with open('Controle_Clientes.txt', 'a') as arquivo:
                arquivo.write(str((f'''
                            Mês: {mes} de {datetime.now().year}
nome: {nome}
idade: {idade}
situação: {pagou}
''')))
            print(f'''
            Mês: {mes}
            nome: {nome}
            idade: {idade}
            situação: {pagou}
            ''')

tela = TelaPython()
tela.iniciar()
