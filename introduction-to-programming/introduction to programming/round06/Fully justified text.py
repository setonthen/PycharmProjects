def main():
    paragraph=get_text()
    num_of_char=int(input('Enter the number of characters per line: '))
    whole_text=make_para(paragraph)
    formatted_text(num_of_char,whole_text)

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

def formatted_text(num,text):
    splitted=text.split(' ')
    print(splitted)
    length=0
    for x in range(len(splitted)):
        length+=len(splitted[x])
    print(length)
    poss_char=length//num
    space_avail=length%(poss_char+1)
    to_print=find_num_of_char(text,length//poss_char+1)
    print(poss_char)
    print(space_avail)
    print(to_print)

def find_num_of_char(list,poss):
    count=0
    tot=0
    for x in range(len(list)):
        if tot<poss:
            tot+=len(list[x])
            count+=1
        else:
            x=len(list)
    return count

main()



