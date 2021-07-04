# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Template for task: ruutu


def main():
    width = int(input("Enter the width for a box: "))
    height = int(input("Enter the height for a box: "))
    mark = input("Enter a print mark: ")
    print()
    print_box(width,height,mark)

def print_box(b,h,sym):
    for col in range(h):
        for row in range(b):
            print(sym,end='')
        print()
main()


