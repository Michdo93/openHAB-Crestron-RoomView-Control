# openHAB-Crestron-RoomView-Control
Control an old Crestron RoomView flash Application with openHAB

<meta name="google-site-verification" content="hVcxzbwKdDidRgph8nCh75lZcwZETa_A62NnpZOzuRY" />

Crestron RoomView is an application for controlling projectors.

![picture alt](https://raw.githubusercontent.com/Michdo93/openHAB-Crestron-Room-View-Control/main/crestron_room_view.JPG)

The given python code will click on different buttons of the Crestron RoomView application. You can remote control it over SSH. This could be embedded in openHAB.

## Preparation

In order to use an old Flash application, an old Flash version must be installed. In addition to installing an old Flash version, you must also install an older browser.

The example was tested on Windows 10 with [Python 3.10](https://www.python.org/downloads/), [Flash Player 10](http://www.oldversion.com.de/mac/adobe-flash-player/), and [Firefox 7](http://www.oldversion.com.de/windows/mozilla-firefox-7-0). I recommend a virtual machine for the application to be accessed externally.

Of course you can also install it on `Linux`.

Please make sure that the virtual machine has an `ssh server` because you have to connect to this virtual machine and run a Python code. For Windows please install the [OpenSSH Server](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui) as optional feature. On Windows you have also to install the [PsTools](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec).

A tip from me is, to install [Git](https://git-scm.com/downloads) on Windows. Then add `C:\Program Files\Git\usr\bin` and `C:\Program Files\Git\cmd` to your `PATH` variable. This allows you to run commands like `nano` or `cat`, which makes using `SSH` much more convenient.

## Installation

At first you have to install `pyautogui`:

```
pip install pyautogui
pip install pillow
```

Maybe on Linux you have to run

```
python3 -m pip install pyautogui
```

On Windows it is definitely

```
python -m pip install pyautogui
```

Then you have to download the `room_view.py` file and place it to a path where you can run it inside your VM. On a Linux VM as example:

```
cd /home/<user>
wget https://raw.githubusercontent.com/Michdo93/openHAB-Crestron-Room-View-Control/main/room_view.py
sudo chmod +x room_view.py
```

On Windows:

```
cd C:\Users\<user>
wget https://raw.githubusercontent.com/Michdo93/openHAB-Crestron-Room-View-Control/main/room_view.py
```

The paths `/home/<user>` or `C:\Users\<user>` are the default paths which are open when you start a ssh session to this VM. Please make sure that you replace `<user>` with your actual username.

## Usage

On Linux you have to run:

```
python3 room_view.py <command>
```

So if you want to connect via `SSH` you have to run:

```
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> 'DISPLAY=:0 python3 room_view.py <command>'
```

For this you have to place

```
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> 'DISPLAY=:0 python3 room_view.py %2$s'
```

to your `/etc/openhab/misc/exec.whitelist`.

If you will run it on Windows you have to run:

```
python room_view.py <command>
```

So if you want to connect via `SSH` you have to run:

```
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> '"C:\Program Files\PSTools\PsExec.exe" -u <user> -p <password> -i 1 -w C:\Users\<user> powershell.exe "<path/to/python.exe> C:\Users\<user>\room_view.py <command>"'
```

For this you have to place

```
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> '"C:\Program Files\PSTools\PsExec.exe" -u <user> -p <password> -i 1 -w C:\Users\<user> powershell.exe "<path/to/python.exe> C:\Users\<user>\room_view.py %2$s"'
```

to your `/etc/openhab/misc/exec.whitelist`.

In the next step you have to create your items in `/etc/openhab/items`. I will give only one example:

```
Switch toggleBeamerPower
```

At least you have to create your rules in `/etc/openhab/rules`. I will give only one example:

```
rule "toggle power button"
when
    Item toggleBeamerPower changed to ON
then
    executeCommandLine("/usr/bin/sshpass","-p","<password>","/usr/bin/ssh","-t","-o","StrictHostKeyChecking=no","<user>@<ip>","C:\Program Files\PSTools\PsExec.exe","-u","<user>","-p","<password>","-i","1","-w","C:\Users\<user>","powershell.exe","<path/to/python.exe>","C:\Users\<user>\room_view.py openFirefox")
    Thread::sleep(15000)  // wait 15 seconds
    executeCommandLine("/usr/bin/sshpass","-p","<password>","/usr/bin/ssh","-t","-o","StrictHostKeyChecking=no","<user>@<ip>","C:\Program Files\PSTools\PsExec.exe","-u","<user>","-p","<password>","-i","1","-w","C:\Users\<user>","powershell.exe","<path/to/python.exe>","C:\Users\<user>\room_view.py togglePower")
end
```

Please make sure that you replace `<user>` with the username of your VM and `<password>` with the password of this user. Also you have to replace `<ip>` with the ip address of the VM. If you are on windows you have to replace `<path/to/python.exe>` and give the path to run python.

## Commands

| Command |  Function | 	Description |
| :-------------: |:-------------:| :-----:|
| openFirefox | openFirefox() | Will open the Firefox browser. Please notice that you have to set it as default browser. |
| closeFirefox | closeFirefox() | Will close the Firefox browser. Therefore it will click on the browser and press <kbd>ALT</kbd> + <kbd>F4</kbd>. |
| togglePower | togglePower() | Will toggle the power of the projector. If it's of the projector will be powered on. |
| reduceVolume | reduceVolume() | Will reduce the volume of the projector by its typical step. |
| increaseVolume | increaseVolume() | Will increase the volume of the projector by its typical step. |
| muteVolume | muteVolume() | Will mute the volume of the projector. |
| changeSourceToComputer1 | changeSourceToComputer1() | Will change the source to Computer1. |
| changeSourceToComputer2 | changeSourceToComputer2() | Will change the source to Computer2. |
| changeSourceToHDMI1 | changeSourceToHDMI1() | Will change the source to HDMI1. |
| changeSourceToHDMI2 | changeSourceToHDMI2() | Will change the source to HDMI2. |
| changeSourceToVideo | changeSourceToVideo() | Will change the source to Video. |


## Troubleshooting

 * You have to make sure that Firefox is your default browser.
 * You have to make sure that Firefox will start in Fullscreen mode. Therefore you can run firefox and activate the fullscreen mode. On the next start the fullscreen mode should automatically be activated.
 * You have to make sure that the virtual machine is starting and the user is logged in. I recommend to autologin the user because pyautogui can only run if the user is logged in.
 
## Known issues

* Sadly you will not receive a feedback from your projector. So you don't know if the projector is really started by a click or if it was already on and you turn it off again.

## Items

You have to add following items:

```
Group Crestron_RoomView_Control "Crestron RoomView Control" <screen>

Switch Crestron_RoomView_Control_OpenFirefox "Open Firefox" (Crestron_RoomView_Control)
Switch Crestron_RoomView_Control_CloseFirefox "Close Firefox" (Crestron_RoomView_Control)
Switch Crestron_RoomView_Control_TogglePower "On/off projector" (Crestron_RoomView_Control)
Switch Crestron_RoomView_Control_VolumeDown "Decrease volume" (Crestron_RoomView_Control)
Switch Crestron_RoomView_Control_VolumeUp "Increase volume" (Crestron_RoomView_Control)
Switch Crestron_RoomView_Control_Mute_Volume "Mute volume" (Crestron_RoomView_Control)
Switch Crestron_RoomView_Control_SrcToComputer1 "Computer1/YPbPr1" (Crestron_RoomView_Control)
Switch Crestron_RoomView_Control_SrcToComputer2 "Computer2/YPbPr2" (Crestron_RoomView_Control)
Switch Crestron_RoomView_Control_SrcToHDMI1 "HDMI1" (Crestron_RoomView_Control)
Switch Crestron_RoomView_Control_SrcToHDMI2 "HDMI2" (Crestron_RoomView_Control)
Switch Crestron_RoomView_Control_SrcToVideo "Video" (Crestron_RoomView_Control)
```

## Rules

The rules can look as example like following:

```
rule "Crestron_RoomView_Control_OpenFirefox changed to ON"
when
    Item Crestron_RoomView_Control_OpenFirefox changed to ON
then
    executeCommandLine("/usr/bin/sshpass","-p","<password>","/usr/bin/ssh","-t","-o","StrictHostKeyChecking=no","<user>@<ip>","C:\Program Files\PSTools\PsExec.exe","-u","<user>","-p","<password>","-i","1","-w","C:\Users\<user>","powershell.exe","<path/to/python.exe>","C:\Users\<user>\room_view.py","openFirefox")
    Crestron_RoomView_Control_OpenFirefox.postUpdate(OFF)
end

rule "Crestron_RoomView_Control_CloseFirefox changed to ON"
when
    Item Crestron_RoomView_Control_CloseFirefox changed to ON
then
    executeCommandLine("/usr/bin/sshpass","-p","<password>","/usr/bin/ssh","-t","-o","StrictHostKeyChecking=no","<user>@<ip>","C:\Program Files\PSTools\PsExec.exe","-u","<user>","-p","<password>","-i","1","-w","C:\Users\<user>","powershell.exe","<path/to/python.exe>","C:\Users\<user>\room_view.py","closeFirefox")
    Crestron_RoomView_Control_CloseFirefox.postUpdate(OFF)
end

rule "Crestron_RoomView_Control_TogglePower changed to ON"
when
    Item Crestron_RoomView_Control_TogglePower changed to ON
then
    Crestron_RoomView_Control_OpenFirefox.sendCommand(ON)
    Thread::sleep(5000)  // wait 5 seconds
    executeCommandLine("/usr/bin/sshpass","-p","<password>","/usr/bin/ssh","-t","-o","StrictHostKeyChecking=no","<user>@<ip>","C:\Program Files\PSTools\PsExec.exe","-u","<user>","-p","<password>","-i","1","-w","C:\Users\<user>","powershell.exe","<path/to/python.exe>","C:\Users\<user>\room_view.py","togglePower")
    Crestron_RoomView_Control_TogglePower.postUpdate(OFF)
    Thread::sleep(15000)  // wait 15 seconds (projector starting time)
    Crestron_RoomView_Control_CloseFirefox.sendCommand(ON)
end

rule "Crestron_RoomView_Control_VolumeDown changed to ON"
when
    Item Crestron_RoomView_Control_VolumeDown changed to ON
then
    Crestron_RoomView_Control_OpenFirefox.sendCommand(ON)
    Thread::sleep(5000)  // wait 5 seconds
    executeCommandLine("/usr/bin/sshpass","-p","<password>","/usr/bin/ssh","-t","-o","StrictHostKeyChecking=no","<user>@<ip>","C:\Program Files\PSTools\PsExec.exe","-u","<user>","-p","<password>","-i","1","-w","C:\Users\<user>","powershell.exe","<path/to/python.exe>","C:\Users\<user>\room_view.py","reduceVolume")
    Crestron_RoomView_Control_VolumeDown.postUpdate(OFF)
    Thread::sleep(3000)
    Crestron_RoomView_Control_CloseFirefox.sendCommand(ON)
end

rule "Crestron_RoomView_Control_VolumeUp changed to ON"
when
    Item Crestron_RoomView_Control_VolumeUp changed to ON
then
    Crestron_RoomView_Control_OpenFirefox.sendCommand(ON)
    Thread::sleep(5000)  // wait 5 seconds
    executeCommandLine("/usr/bin/sshpass","-p","<password>","/usr/bin/ssh","-t","-o","StrictHostKeyChecking=no","<user>@<ip>","C:\Program Files\PSTools\PsExec.exe","-u","<user>","-p","<password>","-i","1","-w","C:\Users\<user>","powershell.exe","<path/to/python.exe>","C:\Users\<user>\room_view.py","increaseVolume")
    Crestron_RoomView_Control_VolumeUp.postUpdate(OFF)
    Thread::sleep(3000)
    Crestron_RoomView_Control_CloseFirefox.sendCommand(ON)
end

rule "Crestron_RoomView_Control_Mute_Volume changed to ON"
when
    Item Crestron_RoomView_Control_Mute_Volume changed to ON
then
    Crestron_RoomView_Control_OpenFirefox.sendCommand(ON)
    Thread::sleep(5000)  // wait 5 seconds
    executeCommandLine("/usr/bin/sshpass","-p","<password>","/usr/bin/ssh","-t","-o","StrictHostKeyChecking=no","<user>@<ip>","C:\Program Files\PSTools\PsExec.exe","-u","<user>","-p","<password>","-i","1","-w","C:\Users\<user>","powershell.exe","<path/to/python.exe>","C:\Users\<user>\room_view.py","muteVolume")
    Crestron_RoomView_Control_Mute_Volume.postUpdate(OFF)
    Thread::sleep(3000)
    Crestron_RoomView_Control_CloseFirefox.sendCommand(ON)
end

rule "Crestron_RoomView_Control_SrcToComputer1 changed to ON"
when
    Item Crestron_RoomView_Control_SrcToComputer1 changed to ON
then
    Crestron_RoomView_Control_OpenFirefox.sendCommand(ON)
    Thread::sleep(5000)  // wait 5 seconds
    executeCommandLine("/usr/bin/sshpass","-p","<password>","/usr/bin/ssh","-t","-o","StrictHostKeyChecking=no","<user>@<ip>","C:\Program Files\PSTools\PsExec.exe","-u","<user>","-p","<password>","-i","1","-w","C:\Users\<user>","powershell.exe","<path/to/python.exe>","C:\Users\<user>\room_view.py","changeSourceToComputer1")
    Crestron_RoomView_Control_SrcToComputer1.postUpdate(OFF)
    Thread::sleep(3000)
    Crestron_RoomView_Control_CloseFirefox.sendCommand(ON)
end

rule "Crestron_RoomView_Control_SrcToComputer2 changed to ON"
when
    Item Crestron_RoomView_Control_SrcToComputer2 changed to ON
then
    Crestron_RoomView_Control_OpenFirefox.sendCommand(ON)
    Thread::sleep(5000)  // wait 5 seconds
    executeCommandLine("/usr/bin/sshpass","-p","<password>","/usr/bin/ssh","-t","-o","StrictHostKeyChecking=no","<user>@<ip>","C:\Program Files\PSTools\PsExec.exe","-u","<user>","-p","<password>","-i","1","-w","C:\Users\<user>","powershell.exe","<path/to/python.exe>","C:\Users\<user>\room_view.py","changeSourceToComputer2")
    Crestron_RoomView_Control_SrcToComputer2.postUpdate(OFF)
    Thread::sleep(3000)
    Crestron_RoomView_Control_CloseFirefox.sendCommand(ON)
end

rule "Crestron_RoomView_Control_SrcToHDMI1 changed to ON"
when
    Item Crestron_RoomView_Control_SrcToHDMI1 changed to ON
then
    Crestron_RoomView_Control_OpenFirefox.sendCommand(ON)
    Thread::sleep(5000)  // wait 5 seconds
    executeCommandLine("/usr/bin/sshpass","-p","<password>","/usr/bin/ssh","-t","-o","StrictHostKeyChecking=no","<user>@<ip>","C:\Program Files\PSTools\PsExec.exe","-u","<user>","-p","<password>","-i","1","-w","C:\Users\<user>","powershell.exe","<path/to/python.exe>","C:\Users\<user>\room_view.py","changeSourceToHDMI1")
    Crestron_RoomView_Control_SrcToHDMI1.postUpdate(OFF)
    Thread::sleep(3000)
    Crestron_RoomView_Control_CloseFirefox.sendCommand(ON)
end

rule "Crestron_RoomView_Control_SrcToHDMI2 changed to ON"
when
    Item Crestron_RoomView_Control_SrcToHDMI2 changed to ON
then
    Crestron_RoomView_Control_OpenFirefox.sendCommand(ON)
    Thread::sleep(5000)  // wait 5 seconds
    executeCommandLine("/usr/bin/sshpass","-p","<password>","/usr/bin/ssh","-t","-o","StrictHostKeyChecking=no","<user>@<ip>","C:\Program Files\PSTools\PsExec.exe","-u","<user>","-p","<password>","-i","1","-w","C:\Users\<user>","powershell.exe","<path/to/python.exe>","C:\Users\<user>\room_view.py","changeSourceToHDMI2")
    Crestron_RoomView_Control_SrcToHDMI2.postUpdate(OFF)
    Thread::sleep(3000)
    Crestron_RoomView_Control_CloseFirefox.sendCommand(ON)
end

rule "Crestron_RoomView_Control_SrcToVideo changed to ON"
when
    Item Crestron_RoomView_Control_SrcToVideo changed to ON
then
    Crestron_RoomView_Control_OpenFirefox.sendCommand(ON)
    Thread::sleep(5000)  // wait 5 seconds
    executeCommandLine("/usr/bin/sshpass","-p","<password>","/usr/bin/ssh","-t","-o","StrictHostKeyChecking=no","<user>@<ip>","C:\Program Files\PSTools\PsExec.exe","-u","<user>","-p","<password>","-i","1","-w","C:\Users\<user>","powershell.exe","<path/to/python.exe>","C:\Users\<user>\room_view.py","changeSourceToVideo")
    Crestron_RoomView_Control_SrcToVideo.postUpdate(OFF)
    Thread::sleep(3000)
    Crestron_RoomView_Control_CloseFirefox.sendCommand(ON)
end
```

## Sitemaps

At least you have to add following to your sitemap:

```
Text label="Crestron RoomView Control" icon="screen" {
    Switch item=Crestron_RoomView_Control_TogglePower label="On/off projector" mappings=[ON="Power"]
    Switch item=Crestron_RoomView_Control_VolumeDown label="Decrease volume" mappings=[ON="Vol -"]
    Switch item=Crestron_RoomView_Control_VolumeUp label="Increase volume" mappings=[ON="Vol +"]
    Switch item=Crestron_RoomView_Control_Mute_Volume label="Mute volume" mappings=[ON="Mute volume"]
    Switch item=Crestron_RoomView_Control_SrcToComputer1 label="Computer1/YPbPr1" mappings=[ON="Computer1/YPbPr1"]
    Switch item=Crestron_RoomView_Control_SrcToComputer2 label="Computer2/YPbPr2" mappings=[ON="Computer2/YPbPr2"]
    Switch item=Crestron_RoomView_Control_SrcToHDMI1 label="HDMI1" mappings=[ON="HDMI1"]
    Switch item=Crestron_RoomView_Control_SrcToHDMI2 label="HDMI2" mappings=[ON="HDMI2"]
    Switch item=Crestron_RoomView_Control_SrcToVideo label="Video" mappings=[ON="Video"]
}
```
