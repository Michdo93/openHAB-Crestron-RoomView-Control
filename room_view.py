import webbrowser
import pyautogui
import time
import sys
from PIL import ImageGrab

pyautogui.FAILSAFE = False
BASE_PATH = 'C:/Users/Admin/openHAB-Crestron-RoomView-Control/images'
ACCURACY = 0.85

def openFirefox(url: str = "<url>"):
    webbrowser.open(url)

def closeFirefox():
    pyautogui.click(x=20, y=20, clicks=1, button="left")
    pyautogui.hotkey("alt", "f4")

def togglePower():
    __clickInsideBrowser()
    __toggleButton("poweron.PNG", "poweron_focused.PNG", "poweroff.PNG", "poweroff_focused.PNG")
    __yesToPowerOff()

def powerOn():
    __clickInsideBrowser()
    __buttonFocused("poweron.PNG", "poweron_focused.PNG")

def powerOff():
    __clickInsideBrowser()
    __buttonFocused("poweroff.PNG", "poweroff_focused.PNG")
    __yesToPowerOff()

def reduceVolume():
    __clickInsideBrowser()
    __buttonFocused('volume_down.PNG', 'volume_down_focused.PNG')

def increaseVolume():
    __clickInsideBrowser()
    __buttonFocused('volume_up.PNG', 'volume_up_focused.PNG')

def muteVolume():
    __clickInsideBrowser()
    __buttonFocusedSelected('mute.PNG', 'mute_focused.PNG', 'mute_selected.PNG', 'mute_selected_focused.PNG')

def changeSourceToComputer1():
    __clickInsideBrowser()
    __sourceUp()
    __buttonFocusedSelected('computer1.PNG', 'computer1_focused.PNG', 'computer1_selected.PNG', 'computer1_selected_focused.PNG')

def changeSourceToComputer2():
    __clickInsideBrowser()
    __sourceUp()
    __buttonFocusedSelected('computer2.PNG', 'computer2_focused.PNG', 'computer2_selected.PNG', 'computer2_selected_focused.PNG')

def changeSourceToHDMI1():
    __clickInsideBrowser()
    __sourceUp()
    __buttonFocusedSelected('hdmi1.PNG', 'hdmi1_focused.PNG', 'hdmi1_selected.PNG', 'hdmi1_selected_focused.PNG')

def changeSourceToHDMI2():
    __clickInsideBrowser()
    __sourceUp()
    __buttonFocusedSelected('hdmi2.PNG', 'hdmi2_focused.PNG', 'hdmi2_selected.PNG', 'hdmi2_selected_focused.PNG')

def changeSourceToVideo():
    __clickInsideBrowser()
    __sourceUp()
    __buttonFocusedSelected('video.PNG', 'video_focused.PNG', 'video_selected.PNG', 'video_selected_focused.PNG')

def changeSourceToSVideo():
    __clickInsideBrowser()
    __sourceDown()
    __buttonFocusedSelected('s-video.PNG', 's-video_focused.PNG', 's-video_selected.PNG', 's-video_selected_focused.PNG')

def source():
    __clickInsideBrowser()
    __buttonFocused('source.PNG', 'source_focused.PNG')

def auto():
    __clickInsideBrowser()
    __buttonFocused('auto.PNG', 'auto_focused.PNG')

def blank():
    __clickInsideBrowser()
    __buttonFocused('blank.PNG', 'blank_focused.PNG')

def enter():
    __clickInsideBrowser()
    __buttonFocused('enter.PNG', 'enter_focused.PNG')

def freeze():
    __clickInsideBrowser()
    __buttonFocused('freeze.PNG', 'freeze_focused.PNG')

def openMenu():
    __clickInsideBrowser()
    __buttonFocused('menu.PNG', 'menu_focused.PNG')

def menuLeft():
    __clickInsideBrowser()
    __buttonFocused('menu_left.PNG', 'menu_left_focused.PNG')

def menuRight():
    __clickInsideBrowser()
    __buttonFocused('menu_right.PNG', 'menu_right_focused.PNG')

def menuUp():
    __clickInsideBrowser()
    __buttonFocused('menu_up.PNG', 'menu_up_focused.PNG')

def menuDown():
    __clickInsideBrowser()
    __buttonFocused('menu_down.PNG', 'menu_down_focused.PNG')

def increaseBrightness():
    __clickInsideBrowser()
    __button('brightness.PNG')
    __increaseBrightnessContrastSharpness()
    __closeBrightnessContrastSharpness()

def increaseContrast():
    __clickInsideBrowser()
    __button('contrast.PNG')
    __increaseBrightnessContrastSharpness()
    __closeBrightnessContrastSharpness()

def increaseSharpness():
    __clickInsideBrowser()
    __button('sharpness.PNG')
    __increaseBrightnessContrastSharpness()
    __closeBrightnessContrastSharpness()

def decreaseBrightness():
    __clickInsideBrowser()
    __button('brightness.PNG')
    __decreaseBrightnessContrastSharpness()
    __closeBrightnessContrastSharpness()

def decreaseContrast():
    __clickInsideBrowser()
    __button('contrast.PNG')
    __decreaseBrightnessContrastSharpness()
    __closeBrightnessContrastSharpness()

def decreaseSharpness():
    __clickInsideBrowser()
    __button('sharpness.PNG')
    __decreaseBrightnessContrastSharpness()
    __closeBrightnessContrastSharpness()

def __sourceDown():
    __buttonSelected('source_down.PNG', 'source_down_selected.PNG')

def __sourceUp():
    __buttonSelected('source_up.PNG', 'source_up_selected.PNG')

def __increaseBrightnessContrastSharpness():
    __buttonSelected('contrastbrightnesssharpness_up.PNG', 'contrastbrightnesssharpness_up_focused.PNG')

def __decreaseBrightnessContrastSharpness():
    __buttonSelected('contrastbrightnesssharpness_down.PNG', 'contrastbrightnesssharpness_down_focused.PNG')

def __closeBrightnessContrastSharpness():
    __buttonSelected('close_brightnesscontrastsharpness.PNG', 'close_brightnesscontrastsharpness_focused.PNG')

def __yesToPowerOff():
    time.sleep(1)
    __buttonFocused("yes.PNG", "yes_focused.PNG")

def __clickInsideBrowser():
    __secureConnectionFailed()
    pyautogui.click(x=25, y=25, clicks=1, button="left")
    time.sleep(1)
    __retrying()

def __retrying():
    retrying = None
    timeout = time.time()

    while retrying == None:
        if time.time() > timeout + 3:
            break
        try:
            retrying = pyautogui.locateOnScreen(BASE_PATH + '/' + 'retrying.PNG', confidence=ACCURACY)
        except Exception as e:
            print(e)

    if retrying is not None:
        pyautogui.click(x=20, y=20, clicks=1, button="left")
        pyautogui.hotkey("f5")
        time.sleep(1)

def __secureConnectionFailed():
    secureConnection = None
    timeout = time.time()

    while secureConnection == None:
        if time.time() > timeout + 3:
            break
        try:
            secureConnection = pyautogui.locateOnScreen(BASE_PATH + '/' + 'secure_connection.PNG', confidence=ACCURACY)
        except Exception as e:
            print(e)

    if secureConnection is not None:
        __button("cancel.PNG")
        time.sleep(1)

def __button(button: str):
    toPressButton = None
    timeout = time.time()

    while toPressButton == None:
        if time.time() > timeout + 2:
            break
        try:
            toPressButton = pyautogui.locateOnScreen(BASE_PATH + '/' + button, confidence=ACCURACY)
        except Exception as e:
            print(e)

    if toPressButton is not None:
        toPressButtonCenter = pyautogui.center(toPressButton)
        pyautogui.click(toPressButtonCenter)

def __buttonFocused(button: str, buttonFocused: str):
    toPressButton = None
    timeout = time.time()

    while toPressButton == None:
        if time.time() > timeout + 2:
            break
        try:
            toPressButton = pyautogui.locateOnScreen(BASE_PATH + '/' + button, confidence=ACCURACY)
        except Exception as e:
            print(e)

    while toPressButton == None:
        if toPressButton is not None or time.time() > timeout + 4:
            break
        try:
            toPressButton = pyautogui.locateOnScreen(BASE_PATH + '/' + buttonFocused, confidence=ACCURACY)
        except Exception as e:
            print(e)

    if toPressButton is not None:
        toPressButtonCenter = pyautogui.center(toPressButton)
        pyautogui.click(toPressButtonCenter)

def __buttonSelected(button: str, buttonSelected: str):
    toPressButton = None
    timeout = time.time()

    while toPressButton == None:
        if time.time() > timeout + 2:
            break
        try:
            toPressButton = pyautogui.locateOnScreen(BASE_PATH + '/' + button, confidence=ACCURACY)
        except Exception as e:
            print(e)

    while toPressButton == None:
        if toPressButton is not None or time.time() > timeout + 4:
            break
        try:
            toPressButton = pyautogui.locateOnScreen(BASE_PATH + '/' + buttonSelected, confidence=ACCURACY)
        except Exception as e:
            print(e)

    if toPressButton is not None:
        toPressButtonCenter = pyautogui.center(toPressButton)
        pyautogui.click(toPressButtonCenter)

def __buttonFocusedSelected(button: str, buttonFocused: str, buttonSelected: str, buttonFocusedSelected: str):
    toPressButton = None
    timeout = time.time()

    while toPressButton == None:
        if time.time() > timeout + 2:
            break
        try:
            toPressButton = pyautogui.locateOnScreen(BASE_PATH + '/' + button, confidence=ACCURACY)
        except Exception as e:
            print(e)

    while toPressButton == None:
        if toPressButton is not None or time.time() > timeout + 4:
            break
        try:
            toPressButton = pyautogui.locateOnScreen(BASE_PATH + '/' + buttonFocused, confidence=ACCURACY)
        except Exception as e:
            print(e)

    while toPressButton == None:
        if toPressButton is not None or time.time() > timeout + 6:
            break
        try:
            toPressButton = pyautogui.locateOnScreen(BASE_PATH + '/' + buttonSelected, confidence=ACCURACY)
        except Exception as e:
            print(e)

    while toPressButton == None:
        if toPressButton is not None or time.time() > timeout + 8:
            break
        try:
            toPressButton = pyautogui.locateOnScreen(BASE_PATH + '/' + buttonFocusedSelected, confidence=ACCURACY)
        except Exception as e:
            print(e)

    if toPressButton is not None:
        toPressButtonCenter = pyautogui.center(toPressButton)
        pyautogui.click(toPressButtonCenter)

def __toggleButton(toggleButton1: str, toggleButton1Alternative: str, toggleButton2: str, toggleButton2Alternative: str):
    toPressButton = None
    timeout = time.time()

    while toPressButton == None:
        if time.time() > timeout + 2:
            break
        try:
            toPressButton = pyautogui.locateOnScreen(BASE_PATH + '/' + toggleButton1, confidence=ACCURACY)
        except Exception as e:
            print(e)

    while toPressButton == None:
        if toPressButton is not None or time.time() > timeout + 4:
            break
        try:
            toPressButton = pyautogui.locateOnScreen(BASE_PATH + '/' + toggleButton1Alternative, confidence=ACCURACY)
        except Exception as e:
            print(e)

    if toPressButton is not None:
        toPressButtonCenter = pyautogui.center(toPressButton)
        pyautogui.click(toPressButtonCenter)
    else:
        timeout = time.time()

        while toPressButton == None:
            if time.time() > timeout + 2:
                break
        try:
            toPressButton = pyautogui.locateOnScreen(BASE_PATH + '/' + toggleButton2, confidence=ACCURACY)
        except Exception as e:
            print(e)

        while toPressButton == None:
            if toPressButton is not None or time.time() > timeout + 4:
                break
            try:
                toPressButton = pyautogui.locateOnScreen(BASE_PATH + '/' + toggleButton2Alternative, confidence=ACCURACY)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    globals()[sys.argv[1]]()
