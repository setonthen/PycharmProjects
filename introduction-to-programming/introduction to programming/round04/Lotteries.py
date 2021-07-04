from fractions import Fraction
def main():
    terminator=0
    tot_balls=int(input('Enter the total number of lottery balls: '))
    drawn_balls=int(input('Enter the number of the drawn balls: '))
    terminator=check_input(tot_balls,drawn_balls)
    if terminator==0:
        result=calculate_probability(tot_balls,drawn_balls)
        print('The probability of guessing all ',drawn_balls,' balls correctly is ',result)

def check_input(tBalls,dBalls):
    if tBalls<1 or dBalls<1:
        print("The number of balls must be a positive number.")
        return 1
    elif dBalls>tBalls:
        print("At most the total number of balls can be drawn.")
        return 1
    else:
        return 0

def calculate_probability(tB,dB):
    val1=factorial(tB)
    val2=factorial(dB)
    val3=factorial(tB-dB)
    possible_comb=Fraction(val1,(val2*val3))
    return Fraction(1,possible_comb)
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

main()








