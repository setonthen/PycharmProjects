#Demo 2:
#Items to observe: Inheritance, composition, states of the objects

import time

class Gripper:
    def __init__(self):
        print ("New gripper instantiated")
        self.state="open"

    def open(self):
        print ("Openning gripper ")
        self.state="open"

    def close(self):
        print ("Closing gripper ")
        self.state="closed"

class Robot:
    def __init__(self,manufacturer,speed):
        self.manufacturer = manufacturer
        self.__speed=speed
        print ("New robot object instantiated")
        self.__updateFirmware()

    def moveRobot(self,distance):
        print ("Moving routine started for robot: " + self.manufacturer)
        time.sleep(distance/self.__speed)
        print ("Moving routine finished for robot: " + self.manufacturer)

    def setSpeed(self,newSpeed):
        done = False
        if newSpeed<=200:
            self.__speed = newSpeed
            print ("New speed set to: "+str(self.__speed))
            done = True
        else:
            print ("Sorry but the speed you request exceeds the limit allowed")

        return done

    def __updateFirmware(self):
        print ("updating Robot firmware....")


class AssemblyRobot(Robot):

    def __init__(self,manufacturer, speed, payload):
        Robot.__init__(self,manufacturer,speed)  #This shows inheritance of AssemblyRobot from Robot class
        self.payload = payload
        self.gripper = Gripper() #This shows composition, AssemblyRobot gripper property is linked to a gripper object


    def pick(self):
        self.gripper.close()
        print ("Pick operation started...")

    def place(self):
        self.gripper.open()
        print ("Place operation started...")

r1 = AssemblyRobot("OMRON",10,5)
r2 = AssemblyRobot("KUKA",100,3)

r1.pick()
print (r1.gripper.state)

print ("---------------------")

r2.moveRobot(200) #notice we invoked moveRobot directly from r2, cause this an inherited method
r2.pick()
r2.place()

#notice we retrieve the gripper state from the robot-->gripper object. Becuase this a case of composition
#notice the gripper objects can go through different transitions: pick, place, etc. and the object gripper will track and have memory of its state
print (r2.gripper.state)
