import time
import pyautogui

def sendMsg():
    time.sleep(5)
    text = open('spambot.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')
sendMsg()
