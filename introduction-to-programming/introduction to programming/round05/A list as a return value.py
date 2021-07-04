def main():
    given_num=int(input('How many numbers do you want to process: '))
    result=input_to_list(given_num)
    to_find=int(input(('Enter the number to be searched: ')))
    find_num(to_find,result)

def input_to_list(num):
    store_num=[]
    print('Enter', num, 'numbers:', sep=' ')
    for x in range(num):
        entered_num=int(input())
        store_num.append(entered_num)
    return store_num
def find_num(val,check):
    available=check.count(val)
    if available!=0:
        print(val,"shows up",available,"times among the numbers you have entered.",sep=' ')
    else:
        print(val,"is not among the numbers you have entered.",sep=' ')
main()


