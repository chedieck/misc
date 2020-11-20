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

def cluster(spread=10):
    while 1:
        x, y = pag.position()
        mx, my = [spread * random.gauss(0, 1) for _ in range(2)]
        pag.moveTo(x + mx, y + my)

cluster()

