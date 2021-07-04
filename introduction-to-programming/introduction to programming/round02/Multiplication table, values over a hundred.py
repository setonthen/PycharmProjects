def main():
    numb=int(input('Choose a number: '))
    s=100/numb
    for x in range(1,int(s+2)):
        result=x*numb
        print(x,'*',numb,'=',result)
main()