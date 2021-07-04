
x=0
y=1
sum1=x+y
numb=int(input('How many Fibonacci numbers do you want? '))
if numb==1:
    print('1.',y)
elif numb==2:
    print('1.', y)
    print('2.', y)
else:
    print('1.', y)
    print('2.', y)
    for t1 in range(numb-2):
        x=y
        y=sum1
        sum1=x+y
        print(str(t1+3)+'.', sum1)





