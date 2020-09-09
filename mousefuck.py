import pyautogui as pag
import math
import os
# simple script to make mouse unusable.

PID = os.getpid()
pag.PAUSE = 0.005
with open("/tmp/mousefuck.pid", "w") as f:
    f.write(str(PID))

wid, hei = pag.size()
midwid, midhei = (wid // 2, hei // 2)
R = min([midwid, midhei]) // 2
quarter = round(math.sqrt(2) * R)

while 1:
    for q in range(4 * quarter):
        x = midwid + round(quarter * math.cos(math.pi * q/(2 * quarter)))
        y = midhei + round(quarter * math.sin(math.pi * q/(2 * quarter)))
        pag.moveTo(x,y)

