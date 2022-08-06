import pyautogui
import pyperclip
import time
from selenium import webdriver
driver = webdriver.Edge(executable_path="D:\\edgedriver_win64\\msedgedriver.exe")
pyautogui.PAUSE = 1
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://www.saopaulomania.com.br/")
# esse é para sites com URL sem caracteres especiais(~, ^, etc...)->pyautogui.write("https://www.saopaulomania.com.br/")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=278, y=300)
pyautogui.click(x=577, y=239)
pyautogui.write("Camisa rosa Feminina")
pyautogui.press("enter")
x, y = pyautogui.position()
print(x, y)