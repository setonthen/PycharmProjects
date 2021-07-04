# Introduction to Programming
# Named parameters


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


def print_box(width,height,border_mark='#',inner_mark=' '):
    for x in range(width):
        print(border_mark,end='')
    print()
    for y in range(height-2):
        print(border_mark,end='')
        for x in range(width-2):
            print(inner_mark,end='')
        print(border_mark)
    for x in range(width):
        print(border_mark,end='')
    print()
    print()

main()

