for x in range(1,13):
    if x==2:
        for y in range(1, 29):
            print(y, '.', x, '.', sep='')
    elif (x==4) or (x==6) or (x==9) or (x==11):
        for y in range(1,31):
            print(y,'.',x,'.', sep='')
    else:
        for y in range(1,32):
            print(y,'.',x,'.', sep='')




