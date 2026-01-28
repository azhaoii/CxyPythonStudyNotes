from gpiozero import Button, LED
import time
from signal import pause

button = Button(26) # Using Raspi-Pi Gpio 26
led = LED(17)       # Gpio 17

#-------------------------------------------------------
# while True:
#     print(button.is_pressed) # if button is pressed, return True or FALSE
#     time.sleep(1)
#-------------------------------------------------------

#-------------------------------------------------------
# while True:
#     time.sleep(0.1) # no use all of cpu

#     if button.is_pressed == True:
#         led.on()
#         print("LED is ON")
#     else:
#         led.off()
#         print("LED is OFF")
#-------------------------------------------------------

button.when_pressed = led.on    # callback function led.on, no use "()"
button.when_released = led.off  # when button is pressed or released, lED will do something

pause()