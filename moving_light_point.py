import radio
from microbit import *
import music

radio.on()

def check_buttons(x, y):

    if button_a.is_pressed() or button_b.is_pressed():
        sleep(700)
        #music.play(music.JUMP_UP)
        if button_a.is_pressed() and button_b.is_pressed():
            music.play(music.JUMP_UP)

            pos_point = y * 5 + x
            radio.send(str(pos_point))
            return x, y

        if button_a.is_pressed():
            display.clear()
            if x == 4 and y == 4:
                x = 0
                y = 0
            elif x <= 3:
                x += 1
            elif x == 4:
                x = 0
                y += 1

        if button_b.is_pressed():
            display.clear()
            if x == 0 and y == 0:
                x = 4
                y = 4
            elif x >= 1:
                x -= 1
            else:
                x = 4
                y -= 1


        return x, y

    else:
        return x, y
x, y = 2, 2
display.set_pixel(x, y, 7)
while True:
    # point navigation

    signal = radio.receive()

    if signal:
        display.scroll(signal)



    x, y = check_buttons(x, y)
    display.set_pixel(x, y, 7)

    if pin_logo.is_touched():
        radio.send("password_over")
        #music.play(music.BA_DING)

