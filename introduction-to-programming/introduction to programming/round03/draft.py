def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")
def repeat_name(name, rep):
    if name=='Yogi':
        for x in range(1,rep):
            if x==1:
                print('Yogi, Yogi ')
            else:
                print('Yogi, Yogi Bear')

    elif name=='Boo':
        for x in range(1,rep):
            if x==1:
                print('Boo Boo, Boo Boo')
            else:
                print('Boo Boo, Boo Boo Bear')
    elif name=='Cindy':
        for x in range(1,rep):
            if x==1:
                print('Cindy, Cindy')
            else:
                print('Cindy, Cindy Bear')

def verse(chorus, name):
    if (chorus=="I know someone you don't know"):
        print(chorus)
        repeat_name(name,2)
        print(chorus)
        repeat_name(name, 3)
        print(chorus)
        repeat_name(name, 1)
main()
