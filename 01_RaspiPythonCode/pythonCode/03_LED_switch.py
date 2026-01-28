from gpiozero import Button, LED
import time
from signal import pause

#-------------------------------------------------------
# button = Button(26, bounce_time=0.05) # ban bounce
# led0 = LED(17)  
# led1 = LED(27) 
# led2 = LED(22)  


# led0.off()
# led1.off()
# led2.off()

# led_index = 0;

# def led_switch():
#     global led_index

#     if (led_index % 3) == 0:
#         led0.on()
#         led1.off()
#         led2.off()
#     elif (led_index % 3) == 1:
#         led0.off()
#         led1.on()
#         led2.off()
#     elif (led_index % 3) == 2:
#         led0.off()
#         led1.off()
#         led2.on()

#     led_index += 1

# button.when_pressed = led_switch
# pause()
#-------------------------------------------------------

button = Button(26, bounce_time=0.05) # ban bounce
led_list = [LED(17), LED(27), LED(22)]
led_index = 0

def reset_leds():
    for led in led_list:    # Turn off all of LED by loop
        led.off()

def led_switch():
    global led_index
    reset_leds()

    led_list[led_index].on()
    led_index += 1

    if led_index == len(led_list):
        led_index = 0

reset_leds()
button.when_pressed = led_switch
pause()
