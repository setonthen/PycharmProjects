def main():
    get_number=[0]*5
    print('Give 5 numbers: ')
    index=0
    while index<5:
        get_number[index]=int(input('Next number: '))
        index+=1
    print('The numbers you entered that were greater than zero were: ')
    for x1 in range(len(get_number)):
        if get_number[x1]>0:
            print(get_number[x1])
main()




