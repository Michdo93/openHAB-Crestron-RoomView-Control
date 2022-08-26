# openHAB-Crestron-RoomView-Control
Control an old Crestron RoomView flash Application with openHAB

Crestron RoomView is an application for controlling projectors.

<meta name="google-site-verification" content="FPSzx8QP409imklzUfdtseBX2hKeTr0J_Ly5Lq3Bs1o" />

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
sudo chmod +x room
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
