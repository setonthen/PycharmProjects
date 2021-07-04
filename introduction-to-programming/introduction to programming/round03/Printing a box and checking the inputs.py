#TIE-02106 Introduction to Programming
# Print a box with input checking
#Mukesh Aryal,268456


def main():

    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width,height,mark)

def print_box(b,h,sym):
    for col in range(h):
        for row in range(b):
            print(sym,end='')
        print()

def read_input(message):
    limit=int(input(message))
    while limit<1:
        limit=int(input(message))
    return limit

main()

