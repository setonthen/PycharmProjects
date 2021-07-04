#TIE-02106 Introduction to Programming
# Area
#Mukesh Aryal,268456

from math import sqrt
def main():
    side_1 = float(input("Enter the length of the first side: "))
    side_2 = float(input("Enter the length of the second side: "))
    side_3 = float(input("Enter the length of the third side: "))
    Area=area(side_1,side_2,side_3)
    print("The triangle's area is ",format(Area,'.1f'),sep='')

def area(a,b,c):
    s=(a+b+c)/2
    A=sqrt(s*(s-a)*(s-b)*(s-c))
    return A

main()
