import webbrowser
import pyautogui
import time
import os
import sys

pyautogui.FAILSAFE = False

def openFirefox():
    webbrowser.open("<url>")

def closeFirefox():
    pyautogui.click(x=20, y=20, clicks=1, button="left")
    pyautogui.hotkey("alt", "f4")

def togglePower():
    pyautogui.click(x=110, y=160, clicks=1, button="left")

def reduceVolume():
    pyautogui.click(x=180, y=160, clicks=1, button="left")

def increaseVolume():
    pyautogui.click(x=530, y=160, clicks=1, button="left")

def muteVolume():
    pyautogui.click(x=410, y=160, clicks=1, button="left")

def changeSourceToComputer1():
    pyautogui.click(x=280, y=280, clicks=1, button="left")

def changeSourceToComputer2():
    pyautogui.click(x=280, y=320, clicks=1, button="left")

def changeSourceToHDMI1():
    pyautogui.click(x=280, y=360, clicks=1, button="left")

def changeSourceToHDMI2():
    pyautogui.click(x=280, y=400, clicks=1, button="left")

def changeSourceToVideo():
    pyautogui.click(x=280, y=440, clicks=1, button="left")

if __name__ == '__main__':
    globals()[sys.argv[1]]()
