import webbrowser
import pyautogui
import time
import os
import sys
from PIL import ImageGrab

pyautogui.FAILSAFE = False

def openFirefox(url: str = "<url>"):
    webbrowser.open(url)

def closeFirefox():
    pyautogui.click(x=20, y=20, clicks=1, button="left")
    pyautogui.hotkey("alt", "f4")

def togglePower():
    __clickInsideBrowser()
    poweron = pyautogui.locateOnScreen('images/poweron.PNG')
    poweron_focused = pyautogui.locateOnScreen('images/poweron_focused.PNG')
    poweroff = pyautogui.locateOnScreen('images/poweroff.PNG')
    poweroff_focused = pyautogui.locateOnScreen('images/poweroff_focused.PNG')

    if poweron is not None:
        poweron_center = pyautogui.center(poweron)
        pyautogui.click(poweron_center)
    elif poweron_focused is not None:
        poweron_focused_center = pyautogui.center(poweron_focused)
        pyautogui.click(poweron_focused_center)
    elif poweroff is not None:
        poweroff_selected_center = pyautogui.center(poweroff)
        pyautogui.click(poweroff_selected_center)
        __yesToPowerOff()
    elif poweroff_focused is not None:
        poweroff_selected_focused_center = pyautogui.center(poweroff_focused)
        pyautogui.click(poweroff_selected_focused_center)
        __yesToPowerOff()

def powerOn():
    __clickInsideBrowser()
    poweron = pyautogui.locateOnScreen('images/poweron.PNG')

    if poweron is not None:
        poweron_center = pyautogui.center(poweron)
        pyautogui.click(poweron_center)
    else:
        poweron_focused = pyautogui.locateOnScreen('images/poweron_focused.PNG')

        if poweron_focused is not None:
            poweron_focused_center = pyautogui.center(poweron_focused)
            pyautogui.click(poweron_focused_center)

def powerOff():
    __clickInsideBrowser()
    poweroff = pyautogui.locateOnScreen('images/poweroff.PNG')

    if poweroff is not None:
        poweroff_center = pyautogui.center(poweroff)
        pyautogui.click(poweroff_center)
    else:
        poweroff_focused = pyautogui.locateOnScreen('images/poweroff_focused.PNG')

        if poweroff_focused is not None:
            poweroff_focused_center = pyautogui.center(poweroff_focused)
            pyautogui.click(poweroff_focused_center)
    __yesToPowerOff()

def __yesToPowerOff():
    time.sleep(1)
    yes = pyautogui.locateOnScreen('images/yes.PNG')

    if yes is not None:
        yes_center = pyautogui.center(yes)
        pyautogui.click(yes_center)
    else:
        yes_focused = pyautogui.locateOnScreen('images/yes_focused.PNG')
        
        if yes_focused is not None:
            yes_focused_center = pyautogui.center(yes_focused)
            pyautogui.click(yes_focused_center)

def reduceVolume():
    __clickInsideBrowser()
    volumedown = pyautogui.locateOnScreen('images/volume_down.PNG')

    if volumedown is not None:
        volumedown_center = pyautogui.center(volumedown)
        pyautogui.click(volumedown_center)
    else:
        volumedown_focused = pyautogui.locateOnScreen('images/volume_down_focused.PNG')

        if volumedown_focused is not None:
            volumedown_focused_center = pyautogui.center(volumedown_focused)
            pyautogui.click(volumedown_focused_center)

def increaseVolume():
    __clickInsideBrowser()
    volumeup = pyautogui.locateOnScreen('images/volume_up.PNG')

    if volumeup is not None:
        volumeup_center = pyautogui.center(volumeup)
        pyautogui.click(volumeup_center)
    else:
        volumeup_focused = pyautogui.locateOnScreen('images/volume_up_focused.PNG')

        if volumeup_focused is not None:
            volumeup_focused_center = pyautogui.center(volumeup_focused)
            pyautogui.click(volumeup_focused_center)

def muteVolume():
    __clickInsideBrowser()
    mute = pyautogui.locateOnScreen('images/mute.PNG')
    mute_focused = pyautogui.locateOnScreen('images/mute_focused.PNG')
    mute_selected = pyautogui.locateOnScreen('images/mute_selected.PNG')
    mute_selected_focused = pyautogui.locateOnScreen('images/mute_selected_focused.PNG')

    if mute is not None:
        mute_center = pyautogui.center(mute)
        pyautogui.click(mute_center)
    elif mute_focused is not None:
        mute_focused_center = pyautogui.center(mute_focused)
        pyautogui.click(mute_focused_center)
    elif mute_selected is not None:
        mute_selected_center = pyautogui.center(mute_selected)
        pyautogui.click(mute_selected_center)
    elif mute_selected_focused is not None:
        mute_selected_focused_center = pyautogui.center(mute_selected_focused)
        pyautogui.click(mute_selected_focused_center)

def changeSourceToComputer1():
    __clickInsideBrowser()
    __sourceUp()
    computer1 = pyautogui.locateOnScreen('images/computer1.PNG')
    computer1_focused = pyautogui.locateOnScreen('images/computer1_focused.PNG')
    computer1_selected = pyautogui.locateOnScreen('images/computer1_selected.PNG')
    computer1_selected_focused = pyautogui.locateOnScreen('images/computer1_selected_focused.PNG')

    if computer1 is not None:
        computer1_center = pyautogui.center(computer1)
        pyautogui.click(computer1_center)
    elif computer1_focused is not None:
        computer1_focused_center = pyautogui.center(computer1_focused)
        pyautogui.click(computer1_focused_center)
    elif computer1_selected is not None:
        computer1_selected_center = pyautogui.center(computer1_selected)
        pyautogui.click(computer1_selected_center)
    elif computer1_selected_focused is not None:
        computer1_selected_focused_center = pyautogui.center(computer1_selected_focused)
        pyautogui.click(computer1_selected_focused_center)

def changeSourceToComputer2():
    __clickInsideBrowser()
    __sourceUp()
    computer2 = pyautogui.locateOnScreen('images/computer2.PNG')
    computer2_focused = pyautogui.locateOnScreen('images/computer2_focused.PNG')
    computer2_selected = pyautogui.locateOnScreen('images/computer2_selected.PNG')
    computer2_selected_focused = pyautogui.locateOnScreen('images/computer2_selected_focused.PNG')

    if computer2 is not None:
        computer2_center = pyautogui.center(computer2)
        pyautogui.click(computer2_center)
    elif computer2_focused is not None:
        computer2_focused_center = pyautogui.center(computer2_focused)
        pyautogui.click(computer2_focused_center)
    elif computer2_selected is not None:
        computer2_selected_center = pyautogui.center(computer2_selected)
        pyautogui.click(computer2_selected_center)
    elif computer2_selected_focused is not None:
        computer2_selected_focused_center = pyautogui.center(computer2_selected_focused)
        pyautogui.click(computer2_selected_focused_center)

def changeSourceToHDMI1():
    __clickInsideBrowser()
    __sourceUp()
    hdmi1 = pyautogui.locateOnScreen('images/hdmi1.PNG')
    hdmi1_focused = pyautogui.locateOnScreen('images/hdmi1_focused.PNG')
    hdmi1_selected = pyautogui.locateOnScreen('images/hdmi1_selected.PNG')
    hdmi1_selected_focused = pyautogui.locateOnScreen('images/hdmi1_selected_focused.PNG')

    if hdmi1 is not None:
        hdmi1_center = pyautogui.center(hdmi1)
        pyautogui.click(hdmi1_center)
    elif hdmi1_focused is not None:
        hdmi1_focused_center = pyautogui.center(hdmi1_focused)
        pyautogui.click(hdmi1_focused_center)
    elif hdmi1_selected is not None:
        hdmi1_selected_center = pyautogui.center(hdmi1_selected)
        pyautogui.click(hdmi1_selected_center)
    elif hdmi1_selected_focused is not None:
        hdmi1_selected_focused_center = pyautogui.center(hdmi1_selected_focused)
        pyautogui.click(hdmi1_selected_focused_center)

def changeSourceToHDMI2():
    __clickInsideBrowser()
    __sourceUp()
    hdmi2 = pyautogui.locateOnScreen('images/hdmi2.PNG')
    hdmi2_focused = pyautogui.locateOnScreen('images/hdmi2_focused.PNG')
    hdmi2_selected = pyautogui.locateOnScreen('images/hdmi2_selected.PNG')
    hdmi2_selected_focused = pyautogui.locateOnScreen('images/hdmi2_selected_focused.PNG')

    if hdmi2 is not None:
        hdmi2_center = pyautogui.center(hdmi2)
        pyautogui.click(hdmi2_center)
    elif hdmi2_focused is not None:
        hdmi2_focused_center = pyautogui.center(hdmi2_focused)
        pyautogui.click(hdmi2_focused_center)
    elif hdmi2_selected is not None:
        hdmi2_selected_center = pyautogui.center(hdmi2_selected)
        pyautogui.click(hdmi2_selected_center)
    elif hdmi2_selected_focused is not None:
        hdmi2_selected_focused_center = pyautogui.center(hdmi2_selected_focused)
        pyautogui.click(hdmi2_selected_focused_center)

def changeSourceToVideo():
    __clickInsideBrowser()
    __sourceUp()
    video = pyautogui.locateOnScreen('images/video.PNG')
    video_focused = pyautogui.locateOnScreen('images/video_focused.PNG')
    video_selected = pyautogui.locateOnScreen('images/video_selected.PNG')
    video_selected_focused = pyautogui.locateOnScreen('images/video_selected_focused.PNG')

    if video is not None:
        video_center = pyautogui.center(video)
        pyautogui.click(video_center)
    elif video_focused is not None:
        video_focused_center = pyautogui.center(video_focused)
        pyautogui.click(video_focused_center)
    elif video_selected is not None:
        video_selected_center = pyautogui.center(video_selected)
        pyautogui.click(video_selected_center)
    elif video_selected_focused is not None:
        video_selected_focused_center = pyautogui.center(video_selected_focused)
        pyautogui.click(video_selected_focused_center)

def changeSourceToSVideo():
    __clickInsideBrowser()
    __sourceDown()
    svideo = pyautogui.locateOnScreen('images/s-video.PNG')
    svideo_focused = pyautogui.locateOnScreen('images/s-video_focused.PNG')
    svideo_selected = pyautogui.locateOnScreen('images/s-video_selected.PNG')
    svideo_selected_focused = pyautogui.locateOnScreen('images/s-video_selected_focused.PNG')

    if svideo is not None:
        svideo_center = pyautogui.center(svideo)
        pyautogui.click(svideo_center)
    elif svideo_focused is not None:
        svideo_focused_center = pyautogui.center(svideo_focused)
        pyautogui.click(svideo_focused_center)
    elif svideo_selected is not None:
        svideo_selected_center = pyautogui.center(svideo_selected)
        pyautogui.click(svideo_selected_center)
    elif svideo_selected_focused is not None:
        svideo_selected_focused_center = pyautogui.center(svideo_selected_focused)
        pyautogui.click(svideo_selected_focused_center)

def source():
    __clickInsideBrowser()
    source = pyautogui.locateOnScreen('images/source.PNG')

    if source is not None:
        source_center = pyautogui.center(source)
        pyautogui.click(source_center)
    else:
        source_focused = pyautogui.locateOnScreen('images/source_focused.PNG')

        if source_focused is not None:
            source_focused_center = pyautogui.center(source_focused)
            pyautogui.click(source_focused_center)

def auto():
    __clickInsideBrowser()
    auto = pyautogui.locateOnScreen('images/auto.PNG')

    if auto is not None:
        auto_center = pyautogui.center(auto)
        pyautogui.click(auto_center)
    else:
        auto_focused = pyautogui.locateOnScreen('images/auto_focused.PNG')

        if auto_focused is not None:
            auto_focused_center = pyautogui.center(auto_focused)
            pyautogui.click(auto_focused_center)

def blank():
    __clickInsideBrowser()
    blank = pyautogui.locateOnScreen('images/blank.PNG')

    if blank is not None:
        blank_center = pyautogui.center(blank)
        pyautogui.click(blank_center)
    else:
        blank_focused = pyautogui.locateOnScreen('images/blank_focused.PNG')

        if blank_focused is not None:
            blank_focused_center = pyautogui.center(blank_focused)
            pyautogui.click(blank_focused_center)

def enter():
    __clickInsideBrowser()
    enter = pyautogui.locateOnScreen('images/enter.PNG')

    if enter is not None:
        enter_center = pyautogui.center(enter)
        pyautogui.click(enter_center)
    else:
        enter_focused = pyautogui.locateOnScreen('images/enter_focused.PNG')

        if enter_focused is not None:
            enter_focused_center = pyautogui.center(enter_focused)
            pyautogui.click(enter_focused_center)

def freeze():
    __clickInsideBrowser()
    freeze = pyautogui.locateOnScreen('images/freeze.PNG')

    if freeze is not None:
        freeze_center = pyautogui.center(freeze)
        pyautogui.click(freeze_center)
    else:
        freeze_focused = pyautogui.locateOnScreen('images/freeze_focused.PNG')

        if freeze_focused is not None:
            freeze_focused_center = pyautogui.center(freeze_focused)
            pyautogui.click(freeze_focused_center)

def openMenu():
    __clickInsideBrowser()
    menu = pyautogui.locateOnScreen('images/menu.PNG')

    if menu is not None:
        menu_center = pyautogui.center(menu)
        pyautogui.click(menu_center)
    else:
        menu_focused = pyautogui.locateOnScreen('images/menu_focused.PNG')

        if menu_focused is not None:
            menu_focused_center = pyautogui.center(menu_focused)
            pyautogui.click(menu_focused_center)

def menuLeft():
    __clickInsideBrowser()
    menu_left = pyautogui.locateOnScreen('images/menu_left.PNG')

    if menu_left is not None:
        menu_left_center = pyautogui.center(menu_left)
        pyautogui.click(menu_left_center)
    else:
        menu_left_focused = pyautogui.locateOnScreen('images/menu_left_focused.PNG')

        if menu_left_focused is not None:
            menu_left_focused_center = pyautogui.center(menu_left_focused)
            pyautogui.click(menu_left_focused_center)

def menuRight():
    __clickInsideBrowser()
    menu_right = pyautogui.locateOnScreen('images/menu_right.PNG')

    if menu_right is not None:
        menu_right_center = pyautogui.center(menu_right)
        pyautogui.click(menu_right_center)
    else:
        menu_right_focused = pyautogui.locateOnScreen('images/menu_right_focused.PNG')

        if menu_right_focused is not None:
            menu_right_focused_center = pyautogui.center(menu_right_focused)
            pyautogui.click(menu_right_focused_center)

def menuUp():
    __clickInsideBrowser()
    menu_up = pyautogui.locateOnScreen('images/menu_up.PNG')

    if menu_up is not None:
        menu_up_center = pyautogui.center(menu_up)
        pyautogui.click(menu_up_center)
    else:
        menu_up_focused = pyautogui.locateOnScreen('images/menu_up_focused.PNG')

        if menu_up_focused is not None:
            menu_up_focused_center = pyautogui.center(menu_up_focused)
            pyautogui.click(menu_up_focused_center)

def menuDown():
    __clickInsideBrowser()
    menu_down = pyautogui.locateOnScreen('images/menu_down.PNG')

    if menu_down is not None:
        menu_down_center = pyautogui.center(menu_down)
        pyautogui.click(menu_down_center)
    else:
        menu_down_focused = pyautogui.locateOnScreen('images/menu_down_focused.PNG')

        if menu_down_focused is not None:
            menu_down_focused_center = pyautogui.center(menu_down_focused)
            pyautogui.click(menu_down_focused_center)

def increaseBrightness():
    __clickInsideBrowser()
    brightness = pyautogui.locateOnScreen('images/brightness.PNG')

    if brightness is not None:
        brightness_center = pyautogui.center(brightness)
        pyautogui.click(brightness_center)
        __increaseBrightnessContrastSharpness()
        __closeBrightnessContrastSharpness()

def increaseContrast():
    __clickInsideBrowser()
    contrast = pyautogui.locateOnScreen('images/contrast.PNG')

    if contrast is not None:
        contrast_center = pyautogui.center(contrast)
        pyautogui.click(contrast_center)
        __increaseBrightnessContrastSharpness()
        __closeBrightnessContrastSharpness()

def increaseSharpness():
    __clickInsideBrowser()
    sharpness = pyautogui.locateOnScreen('images/sharpness.PNG')

    if sharpness is not None:
        sharpness_center = pyautogui.center(sharpness)
        pyautogui.click(sharpness_center)
        __increaseBrightnessContrastSharpness()
        __closeBrightnessContrastSharpness()

def decreaseBrightness():
    __clickInsideBrowser()
    brightness = pyautogui.locateOnScreen('images/brightness.PNG')

    if brightness is not None:
        brightness_center = pyautogui.center(brightness)
        pyautogui.click(brightness_center)
        __decreaseBrightnessContrastSharpness()
        __closeBrightnessContrastSharpness()

def decreaseContrast():
    __clickInsideBrowser()
    contrast = pyautogui.locateOnScreen('images/contrast.PNG')

    if contrast is not None:
        contrast_center = pyautogui.center(contrast)
        pyautogui.click(contrast_center)
        __decreaseBrightnessContrastSharpness()
        __closeBrightnessContrastSharpness()

def decreaseSharpness():
    __clickInsideBrowser()
    sharpness = pyautogui.locateOnScreen('images/sharpness.PNG')

    if sharpness is not None:
        sharpness_center = pyautogui.center(sharpness)
        pyautogui.click(sharpness_center)
        __decreaseBrightnessContrastSharpness()
        __closeBrightnessContrastSharpness()

def __clickInsideBrowser():
    pyautogui.click(x=50, y=50, clicks=1, button="left")

def __sourceDown():
    source_down = pyautogui.locateOnScreen('images/source_down.PNG')

    if source_down is not None:
        source_down_center = pyautogui.center(source_down)
        pyautogui.click(source_down_center)
    else:
        source_down_selected = pyautogui.locateOnScreen('images/source_down_selected.PNG')

        if source_down_selected is not None:
            source_down_selected_center = pyautogui.center(source_down_selected)
            pyautogui.click(source_down_selected_center)

def __sourceUp():
    source_up = pyautogui.locateOnScreen('images/source_up.PNG')

    if source_up is not None:
        source_up_center = pyautogui.center(source_up)
        pyautogui.click(source_up_center)
    else:
        source_up_selected = pyautogui.locateOnScreen('images/source_up_selected.PNG')

        if source_up_selected is not None:
            source_up_selected_center = pyautogui.center(source_up_selected)
            pyautogui.click(source_up_selected_center)

def __increaseBrightnessContrastSharpness():
    brightnesscontrastsharpness_up = pyautogui.locateOnScreen('images/contrastbrightnesssharpness_up.PNG')

    if brightnesscontrastsharpness_up is not None:
        brightnesscontrastsharpness_up_center = pyautogui.center(brightnesscontrastsharpness_up)
        pyautogui.click(brightnesscontrastsharpness_up_center)
    else:
        brightnesscontrastsharpness_up_focused = pyautogui.locateOnScreen('images/contrastbrightnesssharpness_up_focused.PNG')

        if brightnesscontrastsharpness_up_focused is not None:
            brightnesscontrastsharpness_up_focused_center = pyautogui.center(brightnesscontrastsharpness_up_focused)
            pyautogui.click(brightnesscontrastsharpness_up_focused_center)

def __decreaseBrightnessContrastSharpness():
    brightnesscontrastsharpness_down = pyautogui.locateOnScreen('images/contrastbrightnesssharpness_down.PNG')

    if brightnesscontrastsharpness_down is not None:
        brightnesscontrastsharpness_down_center = pyautogui.center(brightnesscontrastsharpness_down)
        pyautogui.click(brightnesscontrastsharpness_down_center)
    else:
        brightnesscontrastsharpness_down_focused = pyautogui.locateOnScreen('images/contrastbrightnesssharpness_down_focused.PNG')

        if brightnesscontrastsharpness_down_focused is not None:
            brightnesscontrastsharpness_down_focused_center = pyautogui.center(brightnesscontrastsharpness_down_focused)
            pyautogui.click(brightnesscontrastsharpness_down_focused_center)

def __closeBrightnessContrastSharpness():
    close_brightnesscontrastsharpness = pyautogui.locateOnScreen('images/close_brightnesscontrastsharpness.PNG')

    if close_brightnesscontrastsharpness is not None:
        close_brightnesscontrastsharpness_center = pyautogui.center(close_brightnesscontrastsharpness)
        pyautogui.click(close_brightnesscontrastsharpness_center)
    else:
        close_brightnesscontrastsharpness_focused = pyautogui.locateOnScreen('images/close_brightnesscontrastsharpness_focused.PNG')

        if close_brightnesscontrastsharpness_focused is not None:
            close_brightnesscontrastsharpness_focused_center = pyautogui.center(close_brightnesscontrastsharpness_focused)
            pyautogui.click(close_brightnesscontrastsharpness_focused_center)

if __name__ == '__main__':
    globals()[sys.argv[1]]()
