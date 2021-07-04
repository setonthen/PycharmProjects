def main():
    numb=int(input('How many numbers would you like to have? '))
    for x in range(1,numb+1):
        if (x%3==0)and(x%7!=0):
            print('zip')
        elif (x%3!=0)and(x%7==0):
            print('boing')
        elif (x%3==0)and(x%7==0):
            print('zip boing')
        else:
            print(x)
main()