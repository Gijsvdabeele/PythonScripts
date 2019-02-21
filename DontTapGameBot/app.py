# http://www.donttap.com/

from PIL import ImageGrab
from pyautogui import click
import keyboard
import time

points = [(10, 10), (170, 10), (330, 10), (500, 10),
          (10, 170), (170, 170), (330, 170), (500, 170),
          (10, 330), (170, 330), (330, 330), (500, 330),
          (10, 500), (170, 500), (330, 500), (500, 500)]
old = time.time()
count = 0

while True:
    if keyboard.is_pressed('q'):
        break
    im = ImageGrab.grab(bbox=(640, 270, 1260, 890))
    for xy in points:
        if im.getpixel(xy) == (0, 0, 0):
            click(640+xy[0], 270+xy[1])
            count += 1

new = time.time()
print(f"Seconds: {new-old}")
print(f"Hits: {count}")
print(f"{count/(new-old)}")