t1="y"
t2="Y"
t3="n"
t4="N"
s1=input('Answer Y or N: ')
while (s1!=t1) and (s1!=t2) and (s1!=t3) and (s1!=t4):
    print('Incorrect entry.')
    s1 = input('Please retry: ')
print('You answered', s1)
