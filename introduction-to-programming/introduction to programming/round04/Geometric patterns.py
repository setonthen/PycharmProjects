# Introduction to Programming
# Geometry


import math
def menu():
    while True:
        answer = input("Enter the pattern's first letter, q stops this (s/r/q): ")
        if answer == "s":
            square_length=float(input("Enter the length of the square's side: "))
            square_length=check_input(square_length,"square's side: ")
            s2=square_circum(square_length)
            sa2=square_area(square_length)
            display(s2,sa2)

        elif answer == "r":
            rl1=float(input("Enter the length of the rectangle's side 1: "))
            rl1=check_input(rl1,"rectangle's side 1: ")
            rl2=float(input("Enter the length of the rectangle's side 2: "))
            rl2=check_input(rl2,"rectangle's side 2: ")
            rc1=rectangle_circumference(rl1,rl2)
            ra1=rectangle_area(rl1,rl2)
            display(rc1,ra1)

        elif answer == "c":
            radius = float(input("Enter the circle's radius: "))
            radius = check_input(radius, "circle's radius: ")
            cc2 = circle_circum(radius)
            ca2 = circle_area(radius)
            display(cc2, ca2)

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability


def main():
    menu()
    print("Goodbye!")


def check_input(length,shape):
    if shape=="circle's radius: ":
        while length <= 0:
            length = float(input("Enter the " + shape))
    while length<=0:
        length=float(input("Enter the length of the "+shape))
    return length

def square_circum(s1):
    return 4*s1

def square_area(sa1):
    return sa1**2

def rectangle_circumference(len1,len2):
    return (len1+len2)*2

def rectangle_area(a,b):
    return a*b

def display(p1,p2):
    print("The total circumference is",format(p1,'.2f'))
    print("The surface area is",format(p2,'.2f'))

def circle_circum(r):
    return 2*(math.pi)*r

def circle_area(r):
    return math.pi*(r**2)

main()