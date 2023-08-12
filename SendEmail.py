import pyautogui
import pyperclip
import time
import webbrowser
from ProcessAutomation import ticker
from DataAnalysis import maxima
from DataAnalysis import minima
from DataAnalysis import atual



#position = pyautogui.position()
#print(position)

url = "https://www.google.com.br"
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

webbrowser.get(chrome_path).open(url)

pyautogui.PAUSE = 5 
pyautogui.click(x=644, y=49)

pyautogui.hotkey("ctrl", "t")

pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

time.sleep(10)

pyautogui.click(x=56, y=205)

pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy("Analises Diarias")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

mensagem = f"""
Prezado Gestor,

Seguem as análises,conforme solicitado, da ação {ticker} referente aos últimos 6 meses:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Cotação atual: R${atual}

Qualquer dúvida, estou a disposição:

atte
"""
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=1288, y=1008)


    