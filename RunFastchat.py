import os
import time
import pyautogui #I am in a hell of my own creation

def fuckingWork():
    os.system("python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5")
    pyautogui.open('fastchat')
    pyautogui.focus('fastchat')
    pyautogui.typewrite('Among us')
    pyautogui.press('enter')
    
    time.sleep(10)
    os.system('exit')
    
fuckingWork()