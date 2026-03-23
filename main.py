#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize the motors and the drive base
left_motor  = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Initialize the sensor
obstacle_sensor = UltrasonicSensor(Port.S4)

ev3.speaker.beep()

# --- Phase 1: Drive forward until an object is detected ---
# We use a simple while loop: "While the distance is greater than 200mm, keep driving"
while obstacle_sensor.distance() > 200:
    robot.drive(200, 0) # Drive at 200mm/s, 0 turn rate
    wait(10)            # Short delay to keep the loop responsive

# --- Phase 2: Spin in a circle ---
robot.stop()
ev3.speaker.beep()

# To spin in place, we give a 0 forward speed and a non-zero turn rate
# This will run until you manually stop the program or add a timer
robot.drive(0, 180)    # 0 speed, 180 degrees per second turn rate

# Keep spinning for 5 seconds
wait(5000) 

robot.stop()
ev3.screen.print("Complete!")

