#type: ignore
from time import sleep
import time
import math
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
from pwmio import PWMOut
from adafruit_motor import servo
buttonstate = "not pressed"
Servo1 = servo.Servo(pwmio.PWMOut(board.D1 , duty_cycle=2 ** 15, frequency=50))     #Servosetup
Servo2 = servo.Servo(pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50))
button = DigitalInOut(board.D7)
button.direction = Direction.INPUT
button.pull = Pull.UP
Bvalue = False
Presscount = 1
led = digitalio.DigitalInOut(board.D4)
led.direction = digitalio.Direction.OUTPUT
while True:
    if button.value == 0 and buttonstate == "not pressed":
        buttonstate = "pressed"     #Debounce
        Bvalue = True
        Presscount = Presscount + 1                  
    if button.value == 1:
        Bvalue = False
        buttonstate = "not pressed"     #Debounce
    if Bvalue == True and Presscount == 0:
        Servo2.angle = 0        #servos reset
        Servo1.angle = 180
        Presscount = 1
        led.value = True       #Power LED on  
    if Bvalue == True and Presscount == 1:
        led.value = False       #Power LED off    
        Presscount = 0
        Servo2.angle = 40
        Servo1.angle = 220      #servos move