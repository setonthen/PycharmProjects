day=3
for x in range(1,13):
    if x == 2:
        for y in range(1,29):
            if y==day:
                print(y, '.', x, '.', sep='')
                day+=7
        if day == 35:
            day =7
        else:
            day = 7 - (35 - day)
    elif (x==4) or (x==6) or (x==9) or (x==11):
        for y in range(1,31):
            if y==day:
                print(y, '.', x, '.', sep='')
                day+=7
        if day ==37:
            day =7
        else:
            day = 7 - (37 - day)
    else:
        for y in range(1,32):
            if y==day:
                print(y, '.', x, '.', sep='')
                day+=7
        if day == 38:
            day = 7
        else:
            day=7-(38-day)

