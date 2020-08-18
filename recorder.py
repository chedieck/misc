import pyautogui
from time import sleep
import subprocess

# Handless recorder for telegram desktop.
# Telegram needs to be fullscreened and
# this script should be on a shorcut for
# it to work. Depends on xrandr.

out = subprocess.check_output("xrandr | grep '*'", shell=True).decode()
resolution = out.lstrip().split()[0]

x, y = map(lambda x: int(int(x) * 0.97), resolution.split('x'))
pyautogui.moveTo(x, y)
sleep(0.5)
pyautogui.mouseDown()
