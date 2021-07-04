p1=input('Bored? (y/n) ')
if (p1=='y')or(p1=='Y'):
    print("Well, let's stop this, then.")
while (p1=='n')or(p1=='N'):
        if (p1=='n')or(p1=='N'):
            p1=input('Bored? (y/n) ')
            if (p1 == 'y') or (p1 == 'Y'):
                print("Well, let's stop this, then.")
while (p1!='n')and(p1!='N')and(p1!='y')and(p1!='Y'):
    print('Incorrect entry.')
    p1 = input('Please retry: ')
    if (p1=='y')or(p1=='Y'):
        print("Well, let's stop this, then.")
    elif (p1=='n')or(p1=='N'):
        while (p1 == 'n') or (p1 == 'N'):
            if (p1 == 'n') or (p1 == 'N'):
                p1 = input('Bored? (y/n) ')
                if (p1 == 'y') or (p1 == 'Y'):
                    print("Well, let's stop this, then.")











