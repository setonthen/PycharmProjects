#TIE-02106 Introduction to Programming
#Aquarium
#Mukesh Aryal,268456

def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")


def verse(chorus, name):
    if name =="Yogi":
        print_chorus(chorus,name)
    elif name =="Boo Boo":
        print_chorus(chorus, name)
    elif name =="Cindy":
        print_chorus(chorus, name)
def repeat_name(name, rep):
    for x in range(rep):
        print(name, ', ',name,' Bear',sep='')
def print_chorus(chorus, name):
    print(chorus)
    print(name,', ',name,sep='')
    print(chorus)
    repeat_name(name, 3)
    print(chorus)
    repeat_name(name, 1)
    print()
main()




