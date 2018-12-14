import RoboPiLib as RPL
import setup

1claw = 8
2claw = 9

def open():
 RPL.servoWrite(1claw, 1500)
 RPL.servoWrite(2claw, 1500)
