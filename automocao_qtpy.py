import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import pyautogui 
import time
from datetime import date

#funções autogui
def abrir_navegador(): 
    #Abre o navegador
    pyautogui.press('win')
    pyautogui.write("Opera")
    pyautogui.press('enter')
    print("Abrindo o navegador")

def abrir_meet_bd():
    #Abre a aula de Linguagem de Fundamentos de banco de dados
    time.sleep(4)
    pyautogui.write("https://meet.google.com/iup-gwvk-prt")
    pyautogui.press('enter')
    print("Entrando na aula")

def abrir_meet_lp():
    #Abre a aula de Linguagem de de programação
    time.sleep(4)
    pyautogui.write("https://meet.google.com/opa-xvgy-uqn")
    pyautogui.press('enter')
    print("Entrando na aula")

def trocar_user(x,y):
    #Trocando o usuário
    time.sleep(3)
    pyautogui.click(x , y, duration=0.25)      
    time.sleep(3)
    pyautogui.press('tab', presses=2)
    pyautogui.press('enter')    

def mutar_micro (): 
    #Muta microfone e câmera 
    time.sleep(5)
    pyautogui.hotkey('ctrlleft','d')
    print("Mutando o microfone")
    #pyautogui.hotkey('ctrlleft','e')

def entrar():
    pyautogui.click(1288, 625, duration=0.25)

def abrir_bd():
    abrir_navegador()
    abrir_meet_bd()
    trocar_user(1825 , 196)
    mutar_micro()
    entrar()

def abrir_lp():
    abrir_navegador()
    abrir_meet_lp()
    trocar_user(1825 , 196)
    mutar_micro()
    entrar()

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        data_em_texto = date.today().strftime('%d/%m/%Y')

        self.topo = 100
        self.esqd = 100
        self.lag = 500
        self.alt = 250
        self.titulo = 'Aulas Cria'

        btn_lp = QPushButton('Linguagem de Programação', self)
        btn_lp.move(50, 100)
        btn_lp.resize(170, 50)
        btn_lp.setStyleSheet('QPushButton {border: 3px solid #fec63e; font-size:8px; padding: 10px 8px; color: #000; line-height: 20px; text-transform: uppercase; font-weight: bold; letter-spacing: .1em}')
        btn_lp.clicked.connect(self.btn_lp_click)

        btn_bd = QPushButton('Fund. Banco de Dados', self)
        btn_bd.move(300, 100)
        btn_bd.resize(170, 50)
        btn_bd.setStyleSheet('QPushButton {border: 3px solid #fec63e; padding: 10px 10px; color: #000; line-height: 20px; text-transform: uppercase; font-weight: bold; letter-spacing: .1em}')
        btn_bd.clicked.connect(self.btn_bd_click)

        txt1 = QLabel(self)
        txt1.setText('Bem-Vindo, Vinicius!')
        txt1.move(189, 15)
        txt1.setStyleSheet('QLabel {font-size: 14px}')
        txt1.resize(200,25)

        txt2 = QLabel(self)
        txt2.setText(f'Qual a aula de hoje ?')
        txt2.move(200, 35)

        txt3 = QLabel(self)
        txt3.setText(data_em_texto)
        txt3.move(220, 60)
        txt3.setStyleSheet('QLabel {font: bold}')
        
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esqd, self.topo, self.lag, self.alt)
        self.setWindowTitle(self.titulo)
        self.show()

    def btn_lp_click(self):
        abrir_lp()
    def btn_bd_click(self):
        abrir_bd()

aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())
