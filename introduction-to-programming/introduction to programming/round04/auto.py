# TIE-02106 Introduction to Programming
# Solution of Program 'Car'
# Mukesh Aryal, aryalm@student.tut.fi, student nr: 268456

from math import sqrt

# This is a text-based menu. You should ONLY touch TODOs inside the menu.
# TODOs in the menu call functions that you have implemented and take care
# of the return values of the function calls.

def menu():
    tank_size  = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " + \
                                 "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    MENU_TEXT =  "1) Fill 2) Drive 3) Quit \n-> "

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input(MENU_TEXT)

        if choice == "1":
           to_fill = read_number("How many liters of gas to fill up? ")
           gas = fill(tank_size,to_fill,gas)

        elif choice == "2":
           new_x = read_number("x: ")
           new_y = read_number("y: ")
           gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
           break

    print("Thank you and bye!")


# This function has three parameters which are all FLOATs:
#       (1) the size of the tank
#       (2) the amount of gas that is requested to be filled in
#       (3) the amount of gas in the tank currently
#
# The parameters have to be in this order.
# The function returns one FLOAT that is the amount of gas in the
# tank AFTER the filling up.
#
# The function does not print anything and does not ask for any
# input.
def fill(size,filling,current_gas):
    if filling<size-current_gas:
        return current_gas+filling
    else:
        return size



# This function has six parameters. They are all floats.
#   (1) The current x coordinate
#   (2) The current y coordinate
#   (3) The destination x coordinate
#   (4) The destination y coordinate
#   (5) The amount of gas in the tank currently
#   (6) The consumption of gas per 100 km of the car
#
# The parameters have to be in this order.
# The function returns three floats:
#   (1) The amount of gas in the tank AFTER the driving
#   (2) The reached (new) x coordinate
#   (3) The reached (new) y coordinate
#
# The return values have to be in this order.
# The function does not print anything and does not ask for any
# input.
def drive(cx1,cy1,dx1,dy1,cur_tank,consump):
    can_cover=cur_tank*dis_cov_per_l(consump)
    to_cover=poss_cover(cx1,cy1,dx1,dy1)
    if to_cover<=can_cover:
        gas_used=to_cover/dis_cov_per_l(consump)
        new_x=dx1
        new_y=dy1
        gas_left=cur_tank-gas_used
    else:
        new_x = cx1 + (can_cover / to_cover * (dx1 - cx1))
        new_y = cy1 + (can_cover / to_cover * (dy1 - cy1))
        gas_left=0.0

    return gas_left,new_x,new_y

def dis_cov_per_l(c100):
    return 100.0/c100

def poss_cover(x1,y1,dx,dy):
    val=sqrt((dx-x1)**2+(dy-y1)**2)
    return val


def read_number(prompt, error_message="Incorrect input!"):

    # This function reads input from the user.
    # Do not touch this function.
    try:
        return float(input(prompt))
    except ValueError as e:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()

main()
