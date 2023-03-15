# Write your code here :-
from microbit import *

import radio
radio.on()

password = [5, 3, 6, 8]
pos_passsword = 0

while True:
    signal = radio.receive()
    print(signal)
    if signal == "12":
        radio.send("enter password")

    if signal == str(password[pos_passsword]):
        pos_passsword += 1


    display.show(Image.SMILE)
#       sleep(1000) 
#       display.clear()


