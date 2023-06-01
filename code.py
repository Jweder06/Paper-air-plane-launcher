#type: ignore
from time import sleep
import time
import math
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
from pwmio import PWMOut
from adafruit_motor import servo
Servo1 = servo.Servo(pwmio.PWMOut(board.D1 , duty_cycle=2 ** 15, frequency=50))
Servo2 = servo.Servo(pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50))
while True:
    Servo2.angle = 0
    Servo1.angle = 0
    time.sleep(1)
    Servo2.angle = 180
    Servo1.angle = 180
    time.sleep(1)

while True:
#    Servo1.angle = 70
#    Servo2.angle = 70