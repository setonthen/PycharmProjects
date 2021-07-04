
def main():
    schedule=[630,1015,1415,1620,1720,2000]
    time_now=int(input('Enter the time (as an integer): '))
    index=0
    x1=0
    while x1<5:
        if time_now<=schedule[0]:
            index=0
            x1=5
        elif time_now>schedule[5]:
            index=6
            x1=5
        elif time_now>schedule[x1] and time_now<=schedule[x1+1]:
            index=x1+1
            x1=5
        else:
            x1+=1
    print('The next buses leave: ')
    count=3
    while index<6 and count>0:
        print(schedule[index])
        index+=1
        count-=1
    if count>0:
        for x in range(count):
            print(schedule[x])


main()


