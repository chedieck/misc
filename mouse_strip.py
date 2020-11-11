import pyautogui as pag
import math
import random
import os
# simple script to make mouse unusable.

PID = os.getpid()
pag.PAUSE = 0.005
with open(f"/tmp/mousefuck.{PID}.pid", "w") as f:
    f.write(str(PID))

wid, hei = pag.size()
while 1:
    _, y = pag.position()
    x = random.randint(0, wid - 1)
    pag.moveTo(x, y)

