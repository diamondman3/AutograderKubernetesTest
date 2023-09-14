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


"""
Here's the error:

Traceback (most recent call last):
  File "/home/jovyan/AutograderKubernetesTest/RunFastchat.py", line 3, in <module>
    import pyautogui #I am in a hell of my own creation
  File "/opt/conda/lib/python3.10/site-packages/pyautogui/__init__.py", line 246, in <module>
    import mouseinfo
  File "/opt/conda/lib/python3.10/site-packages/mouseinfo/__init__.py", line 223, in <module>
    _display = Display(os.environ['DISPLAY'])
  File "/opt/conda/lib/python3.10/os.py", line 680, in __getitem__
    raise KeyError(key) from None
KeyError: 'DISPLAY'


Maybe I shouldn't fuck around with a library I don't have the slightest clue how to use
"""