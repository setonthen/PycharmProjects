def main():
    paragraph=get_text()
    num_of_char=int(input('Enter the number of characters per line: '))
    whole_text=make_list(paragraph)
    formatted_text(whole_text,num_of_char)

def get_text():
    print('Enter text rows. Quit by entering an empty row.')
    para=[]
    text='a'
    while text!='':
        text=input('')
        para.append(text.strip())
    return para

def make_para(text):
    para=''
    for x in range(len(text)):
        para+=text[x]
        para+=' '
    return para.strip()

def make_list(para):
    text=make_para(para)
    splitted=text.split(' ')
    try:
        without_space=splitted.remove(' ')
    except ValueError:
        without_space=splitted
    return without_space

def formatted_text(list,num):
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

main()
