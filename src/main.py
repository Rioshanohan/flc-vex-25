# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Rohan                                                        #
# 	Created:      11/1/2024, 10:13:28 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

#config
lf_drive = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
lr_drive = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
rf_drive = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True)
rr_drive = Motor(Ports.PORT14, GearSetting.RATIO_18_1, True)

l_intake = Motor(Ports.PORT15, GearSetting.RATIO_18_1, False)
r_intake = Motor(Ports.PORT16, GearSetting.RATIO_18_1, True)

hook_motor = Motor(Ports.PORT17, GearSetting.RATIO_36_1, False)

intake = MotorGroup(l_intake, r_intake)

left_drive = MotorGroup(lf_drive, lr_drive)
right_drive = MotorGroup(rf_drive, rr_drive)

drivetrain = DriveTrain(left_drive, right_drive, units = DistanceUnits.CM)

controller = Controller()

def drive(y, x):
    l_speed = y + x
    r_speed = y - x
    left_drive.spin(FORWARD, l_speed, PERCENT)
    right_drive.spin(FORWARD, r_speed, PERCENT)


def auton():
    drive(100,0)
    intake.spin(FORWARD, 100, PERCENT)
    wait(1, SECONDS)
    drive(0, 0)
    intake.stop(COAST)
    pass

def teleop():
    while True:
        #periodic loop
        wait(20, MSEC)
        #drive
        drive(controller.axis3.position(), controller.axis1.position())
        #intake
        if controller.buttonL1.pressing():
            intake.spin(FORWARD, 100, PERCENT)
        elif controller.buttonL2.pressing():
            intake.spin(REVERSE, 100, PERCENT)
        else:
            intake.stop(COAST)
        #hook
        if controller.buttonR1.pressing():
            hook_motor.spin(FORWARD, 100, PERCENT)
        elif controller.buttonR2.pressing():
            hook_motor.spin(REVERSE, 100, PERCENT)
        else:
            hook_motor.stop(BRAKE)


comp = Competition(teleop, auton)