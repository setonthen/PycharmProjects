def main():
    get_number=[0]*5
    print('Give 5 numbers: ')
    index=0
    while index<5:
        get_number[index]=int(input('Next number: '))
        index+=1
    print('The numbers you entered, in reverse order: ')
    for x in range(len(get_number)-1,-1,-1):
        print(get_number[x])
main()

