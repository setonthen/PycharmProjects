# TIE-02106 Introduction to Programming
# Solution of task  Fully justified text
# Ujjwal Aryal, aryalu@student.tut.fi, student nr: 268447

def toprint():
    list_message=[]
    while True:
        item=input()
        if item=='':
            break
        else:
            list_item=item.split()
            for elements in list_item:
                list_message.append(elements)
    print(list_message)
    return list_message

def format(list,num):
    string = ''
    for start in range(len(list)):
        if len(string) + len(list[start]) < num :
            string += list[start] + ' '
        elif len(string) + len(list[start]) == num:
            string += list[start]
            print(add_space(string,num))
            string=''
        else:
            string=string.rstrip()
            print(add_space(string,num))
            string = list[start] + ' '
    print(string)


def add_space(string,num):
    space_num=string.count(' ')
    space_need=num-len(string)
    int_space=space_need//space_num
    remainder_space=space_need%space_num
    spa_ind_list=spaceing(string)
    count=0
    for item in spa_ind_list:
        string=string[:(item+count*int_space)]+' '*int_space+string[(item+count*int_space):]
        count+=1

    count=0
    for repeat in range(remainder_space):
        new_index=spa_ind_list[repeat]+repeat*int_space+count
        string=string[:new_index]+' '+string[new_index:]
        count+=1
    return string

def spaceing(string):
    list = []
    for number in range(len(string)):
        if string[number]==' ':
            list.append(number)
    return list



def main():
    print('Enter text rows. Quit by entering an empty row.')
    msg=toprint()
    wordsperline=int(input('Enter the number of characters per line: '))
    format(msg,wordsperline)
main()