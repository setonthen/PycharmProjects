#Demo 1 2020:
# Items to observe: classes, objects, constructor, attributes, methods, encapsulation, printing,  casting, time

import time

class Robot:

    #Class constructor
    def __init__(self,manufacturer,speed):
        self.manufacturer=manufacturer
        self.__speed=speed #private variable
        print("New robot object instantiated")
        self.__updateFirmware()

        #To modify private variables we can expose them through a public method
        #There we can place some safety constraints
    def setSpeed(self,newSpeed):
        done=False
        if (newSpeed<=200): # if/else is a very common control flow statement
            self.__speed=newSpeed
            print("New speed set to:"+str(self.__speed))  #casting a numeric value to string
            done=True
        else:
            print("Sorry but the speed you requested exceeds the allowed limit")

        return done

    def getSpeed(self):
        return self.__speed

    def moveRobot(self,distance):
        print ("Moving routine started...")
        time.sleep(distance/self.__speed)
        print("Moving routine finished")

    #private method
    def __updateFirmware(self):
        print("updating Robot firmware")
        time.sleep(2)
        print("Robot firmware updated finished")

r1=Robot("ABB",20)
r1.manufacturer="FANUC"
isSpeedSet=r1.setSpeed(40) #40 mm/s

print (r1.manufacturer)
#Notice that we cannot access private properties
#print (r1.__speed)

print (r1.getSpeed())

if isSpeedSet:
    r1.moveRobot(200) # 200 mm

