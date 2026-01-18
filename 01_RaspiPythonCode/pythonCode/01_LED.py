from gpiozero import LED
import time

led = LED(17)

# while(True):
#    led.on()        # set led on
#    time.sleep(1)   # delay 1s
#    led.off()       # set led off
#    time.sleep(1)
while(True):
    user_cmd = int(input("Input Commad for contorl LED, 1 is ON, 0 is OFF, -1 is exit program:"))
    if user_cmd == 0:
        led.off()
    elif user_cmd == 1:
        led.on()
    elif user_cmd == -1:
        print("Exit Program")
        exit()
    else:
        print("Error command, must 0 or 1 0r -1")
    time.sleep(1)
