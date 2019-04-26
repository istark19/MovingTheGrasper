import RoboPiLib as RPL
import setup
import time
from time import sleep

startloop = 1
leftact = 8
rightact = 9
start_time = time.time()

def right_open():
        RPL.servoWrite(rightact,1000)

def left_open():
        RPL.servoWrite(leftact,1000)

def right_close():
        RPL.servoWrite(rightact,1500)

while True:



        #RPL.servoWrite(8,1000)
        #RPL.servoWrite(9,1000)
        #time.sleep(3)
        #RPL.servoWrite(8,1400)
        #RPL.servoWrite(9,1400)

#       while (time.time() - start_time) % 2 == 0 and (time.time() - start_time$
        while (time.time() - start_time) <= 3 :
                right_open()
                left_open()
                #RPL.servoWrite(8,1000)
                #RPL.servoWrite(9,1000)
        #       print(time.time() - start_time)
                    #right_open()
                #left_open()
        #while (time.time() - start_time) % 4 == 0:
        while (time.time() - start_time) >= 3 and (time.time() - start_time <= $
                #RPL.servoWrite(8,1500)
                #RPL.servoWrite(9,1500)
                right_close()
                left_close()

        while (time.time() - start_time) >= 6:
          start_time = time.time()
        #       print(time.time() - start_time)
                #right_close()
                #left_close()


