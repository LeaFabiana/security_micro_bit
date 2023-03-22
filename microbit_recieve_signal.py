# Write your code here :-
from microbit import *
import radio
import music
radio.on()

password = "101315"

enter_password = False
received_password = ""

while True:
    pos_point = radio.receive()

    if pos_point == "12":
        radio.send("enter password")
        enter_password = True

    while enter_password:
        passwo = radio.receive()
        if passwo == "password_over":
            # music.pitch(440, 100)

            if received_password == password:
                radio.send("you may enter")
                music.play(music.POWER_UP)
                break
            else:
                #music.pitch(100,100)
                #        display.scroll(received_password)
                radio.send("go away")


                music.play(music.JUMP_UP)
        else:

            if passwo:
                received_password += passwo




