def print_box(row,col,border_mark='#',inner_mark='2'):
    for x in range(row):
        print(border_mark,end='')
    print()
    for y in range(col-2):
        print(border_mark,end='')
        for x in range(row-2):
            print(inner_mark,end='')
        print(border_mark)
    for x in range(row):
        print(border_mark,end='')
    print()
    print()


print_box(3, 8, "*")