# Alertar e pedir informação no PyAutoGUI
import pyautogui
senha = pyautogui.password(text="Digite sua senha: ", title="Dados de Login", mask="*")
print(senha)
pyautogui.alert(text="Iniciando sua automação...", title="Automação de Login", button="Ok")

# Pedir informação
email = pyautogui.prompt(text="Digite seu e-mail", title="informações obrigatórias")
print(f"Você digitou {email}")

# Confirmar se algo deve ou não acontecer
resposta = pyautogui.confirm(text="Continuar rodando nossa automação?", title="Confirmação", buttons=["Sim", "Não", "Cancelar"])
if resposta == "Sim":
    print("Continuando automação...")
elif resposta == "Não":
    print("Encerrando automação...")
else:
    print("Operação cancelada.")