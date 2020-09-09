import pyautogui as pag
import math
# simple script to make mouse unusable.

pag.PAUSE = 0.005

wid, hei = pag.size()
midwid, midhei = (wid // 2, hei // 2)
R = min([midwid, midhei]) // 2
quarter = round(math.sqrt(2) * R)

while 1:
    for q in range(4 * quarter):
        x = midwid + round(quarter * math.cos(math.pi * q/(2 * quarter)))
        y = midhei + round(quarter * math.sin(math.pi * q/(2 * quarter)))
        pag.moveTo(x,y)
