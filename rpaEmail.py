import pyautogui
import time
import pandas as pd
import pyperclip

# pyautogui.write() -> escreve
# pyautogui.click -> clica
# pyautogui.locateOnScreen -> identifica uma imagem na sua tela
# pyautogui.hotkey -> usa atalhos do teclado (combinação de teclas)
# pyautogui.press -> aperta um botão do teclado
# print(pyautogui.KEYBOARD_KEYS)

pyautogui.alert('O código vai começar. Não mexa em NADA enquanto o código tiver rodando. Quando finalizar, eu te aviso')

pyautogui.PAUSE = 1
# apertar o windows do teclado
pyautogui.press('win')
# digitar chrome
pyautogui.write("chrome")
# apertar enter
pyautogui.press('enter')

# entrar no Gmail
pyautogui.write('gmail ')
pyautogui.press('enter')

#esperar carregar o google
while not pyautogui.locateOnScreen('google.png', confidence=0.9):
    time.sleep(1)

# localizar a imagem -> vai te dar 4 informações: posicao x, posicao y, largura e altura
x, y, largura, altura = pyautogui.locateOnScreen('google.png', confidence=0.9)
# clicar no meio da imagem
pyautogui.click(x + largura/2, y + altura/2)

time.sleep(5)

# entrar em contatos
x, y, largura, altura = pyautogui.locateOnScreen('pontinhos.png', confidence=0.9)
pyautogui.click(x + largura/2, y + altura/2)

time.sleep(1)
x, y, largura, altura = pyautogui.locateOnScreen('contatos.png', confidence=0.9)
pyautogui.click(x + largura/2, y + altura/2)

time.sleep(3)

# exportar os contatos
x, y, largura, altura = pyautogui.locateOnScreen('exportar.png')
pyautogui.click(x + largura/2, y + altura/2)
x, y, largura, altura = pyautogui.locateOnScreen('confirmar_exportar.png')
pyautogui.click(x + largura/2, y + altura/2)


# enviando email
time.sleep(2)
df = pd.read_csv('contacts.csv')
df = df.dropna(axis=1)

pyautogui.hotkey('ctrl', 'pgup')

for email in df['E-mail 1 - Value']:
    x, y, largura, altura = pyautogui.locateOnScreen('escrever.png')
    pyautogui.click(x + largura / 2, y + altura / 2)

    # escrever o email
    pyautogui.write(email)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.write('Email teste')
    pyautogui.press('tab')
    texto = '''
    Testando o envio de email

    está tudo certo

    ou não ?
    '''
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 'enter')

    pyautogui.alert('O código terminou, pode pegar o seu computador de volta')


# descobrir posição do mouse
print(pyautogui.position())
pyautogui.click(x, y)


# dar alt tab para achar uma janela
while not pyautogui.locateOnScreen('ibexpert.png', confidence=0.3):
    pyautogui.hotkey('alt', 'shift', 'tab')
print("Achei o paint")
