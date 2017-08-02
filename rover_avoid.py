# Attach: SR-04 Range finder, switch on SW1, and of course motors.

# The switch SW2 stops and starts the robot

from rrb3 import *
import time, random

BATTERY_VOLTS = 9
MOTOR_VOLTS = 6
MOTOR_SPEED = 0.45
DISTANCE_THRESHOLD = 40

rr = RRB3(BATTERY_VOLTS, MOTOR_VOLTS)

# if you dont have a switch, change the value below to True
running = True #False

def get_avg_distance():
    sample_rate = 5
    distance = 0
    for _ in range(sample_rate):
        distance += rr.get_distance()
    return distance/sample_rate

def turn_randomly():
    turn_time = random.randint(2, 4)
    turn_time = turn_time/2;
    if random.randint(1, 2) == 1:
        rr.set_led1(1)
        rr.left(turn_time, MOTOR_SPEED) # turn at half speed
        rr.set_led1(0)
    else:
        rr.set_led2(1)
        rr.right(turn_time, MOTOR_SPEED)
        rr.set_led2(0)
    rr.stop()

try:
    while True:
        distance = get_avg_distance()
        print(distance)
        if distance < DISTANCE_THRESHOLD and running:
            turn_randomly()
        if running:
            rr.forward(0, MOTOR_SPEED)
        if rr.sw2_closed():
            running = not running
        if not running:
            rr.stop()
        time.sleep(0.1)
finally:
    print("Exiting")
    rr.cleanup()
