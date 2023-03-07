# Write your code here :-)
import radio
from microbit import *

radio.on()
# radio.config(groupe=10)

x = 3
y = 1
while True:

    display.set_pixel(x, y, 7)
    if button_a.get_presses():
        display.clear()
        if x == 4 and y == 4:
            x = 0
            y = 0
        elif x <= 3:
            x += 1
        elif x == 4:
            x = 0
            y += 1

    if button_b.get_presses():
        display.clear()
        if x == 0 and y == 0:
            x = 4
            y = 4

        elif x >= 1:
            x -= 1
        else:
            x = 4
            y -= 1
    if pin0.is_touched():
        r = y*5+x
        radio.send(str(r))


