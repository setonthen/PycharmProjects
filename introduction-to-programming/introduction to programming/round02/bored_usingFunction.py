
p1=input('Bored? (y/n) ')
def when_y():
    if (p1 == 'y') or (p1 == 'Y'):
        print("Well, let's stop this, then.")
when_y()
def when_n():
    if (p1 == 'n') or (p1 == 'N'):
        while (p1=='n')or(p1=='N'):
            p1=input('Bored? (y/n) ')
            when_y()
when_n()
while (p1!='n')and(p1!='N')and(p1!='y')and(p1!='Y'):
                while (p1!='y')and(p1!='Y')and(p1!='n')and(p1!='N'):
                    print('Incorrect entry.')
                    p1 = input('Please retry: ')
                    when_y()
                    if (p1=='n')or(p1=='N'):
                        when_n()
