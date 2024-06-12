# DESAFIO
'''
Crie um programa que pede ao usuário e senha, 
e na sequência, 
copia e cola o usuário e senha dentro de um bloco de notas
'''
import pyautogui
email = pyautogui.prompt(text="Digite seu e-mail", title="informações obrigatórias")
senha = pyautogui.password(text="Digite sua senha: ", title="Dados de Login", mask="*")

pyautogui.click(2458,101, duration=2)
pyautogui.typewrite(email)
pyautogui.press("enter")
pyautogui.typewrite(senha)