# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task auto_luokkana, program code template

MENU_TEXT =  "1) Fill 2) Drive 3) Quit \n-> "
CAR_TEXT = "The tank contains {:.1f} liters of gas and " + \
           "the odometer shows {:.1f} kilometers."


# Class Car: Implements a car that moves a certain distance and can be 
# filled. The class defines what is the car like: what information it 
# contains and what operations can be carried out for it.
class Car:
    
    # Method: constructor, initiates the object (tank is empty and 
    # location is 0, 0)
    # Parameter: tank_size, the size of this car's tank
    # Parameter: gas_consumption, how much gas this car consumes when it
    #            drives a 100 kilometers 
    def __init__(self, tank_size, gas_consumption):
        self.__tank_size = tank_size
        self.__gas_consumption = gas_consumption
        self.__gas=0
        self.__odometer=0

    def fill(self,amount):
        if amount<=self.__tank_size-self.__gas and amount>=0:
            self.__gas+=amount
        elif amount>self.__tank_size-self.__gas:
            self.__gas=self.__tank_size
        elif amount<0:
            print('You cannot remove gas from the tank')

    def drive(self,amount):
        if amount>=0:
            to_reduce=(self.__gas_consumption/100)*amount
            if to_reduce<self.__gas:
                self.__gas-=to_reduce
                self.__odometer=amount
            elif self.__gas==0 or to_reduce==0:
                self.__odometer=self.__odometer
            else:
                self.__gas=0
                self.__odometer=(100/self.__gas_consumption)*amount
        else:
            print('You cannot travel a negative distaince')
    def printInformation(self):
        print('The tank contains '+str((format(self.__gas,'.1f'))+
              ' liters of gas and the odometer shows '
                +str(format(self.__odometer,'.1f'))+' kilometers.'))

    # TODO: Insert here the definitions of all other methods of this class.
    # The methods are a part of the class. Therefore, they are intended on 
    # this level (=inside the class definition).

    
def main():

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas_consumption = read_number("How many liters of gas does the car " + \
                                  "consume per hundred kilometers? ")
    
    # Here we define the variable car which is an object initiated from the
    # class Car. This is the line where the constructor of the class Car
    # (the method that is named __init__) is called!
    car = Car(tank_size, gas_consumption)
    
    # (In this program we only need one car-object but it is possible
    # to create multiple objects from one class. For example we could
    # create two objects:
    # lightning_mcqueen = Car(20, 30)
    # mater = Car(10, 10) )

    while True:
        car.printInformation()
        choice = input(MENU_TEXT)
        if choice == "1":
           to_fill = read_number("How many liters of gas to fill up? ")
           # TODO: call the fill-method for the car-object here (task b)
           car.fill(to_fill)
        elif choice == "2":
           distance = read_number("How many kilometers to drive? ")
           # TODO: call the drive-method for the car-object here (task c)
           car.drive(distance)
        elif choice == "3":
           break
    print("Thank you and bye!")


def read_number(prompt, error_message="Incorrect input!"):

    # This function reads input from the user.
    # Do not touch this function.
    try:
        return float(input(prompt))
    except ValueError as e:
        print(error_message)
        return read_number(prompt, error_message)


main()
