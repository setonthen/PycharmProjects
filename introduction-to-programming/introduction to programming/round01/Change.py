
price0=int(input('Purchase price: '))
paid0=int(input('Paid amount of money: '))
return0=paid0-price0

if return0!=0:
    print('Offer change:')
    n1=return0//10
    if n1!=0:
        print(n1,'ten-euro notes')
    n2=(return0%10)//5
    if n2!=0:
        print(n2,'five-euro notes')
    n3=((return0%10)%5)//2
    if n3!=0:
        print(n3,'two-euro coins')
    n4=(((return0%10)%5)%2)//1
    if n4!=0:
        print(n4,'one-euro coins')
else:
    print('No change')
