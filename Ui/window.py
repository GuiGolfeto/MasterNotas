from PySimpleGUI import PySimpleGUI as sg
import automation.atomatic as i


class screenCadastroNF:
    def __init__(self):
        sg.theme('DarkBlue12')
        layout = [
            [sg.Column([[sg.Text('', size=(0, 1))]])],
            
            [sg.Column([[sg.Text('', size=(32, 0))]]),
             sg.Image(filename='./logo.png')],
            
            [sg.Column([[sg.Text('', size=(0, 2))]])],
            
            [sg.Column([[sg.Text('', size=(2, 0))]]),
             sg.Text('Ordem de Serviço', font=('Arial', 30), size=(15, 0)), sg.Input(size=(15, 0), font=('Arial', 25), key='ordemSvc')],
            
            [sg.Column([[sg.Text('', size=(2, 0))]]),
             sg.Text('NF de Remessa', font=('Arial', 30), size=(15, 0)), sg.Input(size=(15, 0), font=('Arial', 25), key='NFremessa')],
            
            [sg.Column([[sg.Text('', size=(2, 0))]]),
             sg.Text('NF e Retorno', font=('Arial', 30), size=(15, 0)), sg.Input(size=(15, 0), font=('Arial', 25), key='NFretorno')],
            
            [sg.Column([[sg.Text('', size=(2, 0))]]),
             sg.Text('Preço', font=('Arial', 30), size=(15, 0)), sg.Input(size=(15, 0), font=('Arial', 25), key='price')],
            
            [sg.Column([[sg.Text('', size=(2, 0))]]),
             sg.Text('Descrição', font=('Arial', 30), size=(15, 0)), sg.Multiline(size=(20, 4), font=('Arial', 18), key='desc')],
            
            [sg.Column([[sg.Text('', size=(0, 1))]])],
                      
            [sg.Column([[sg.Text('', size=(2, 0))]]),
             sg.Button('Enviar dados', font=('Arial', 18)),
             sg.Button('Limpar dados', font=('Arial', 18))],
            [sg.Column([[sg.Text('', size=(2, 0))]]),
             sg.Button('Sair', font=('Arial', 18))],

        ]
        self.janela = sg.Window('Lançamento de NFs', size = (750,700)).layout(layout)
        
        

    def iniciarAuto(self):
        while True:
            self.button, self.values = self.janela.Read()
            
            if self.button == "Sair":
                sg.WIN_CLOSED
                break
            
            if self.button == "Limpar dados":
                self.janela['ordemSvc']('')
                self.janela['NFremessa']('')
                self.janela['NFretorno']('')
                self.janela['price']('')
                self.janela['desc']('')

            if self.button == "Enviar dados":
                ordem = self.values['ordemSvc']
                NFremessa = self.values['NFremessa']
                NFretorno = self.values['NFretorno']
                price = self.values['price']
                desc = self.values['desc']
                
                i.navegador(desc, price, ordem, NFremessa, NFretorno)