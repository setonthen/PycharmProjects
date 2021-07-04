def main():
    file_name=input('Enter the name of the file: ')
    lines = read_message()
    to_write=open(file_name,'a')
    line_num=1
    for index in range(len(lines)):
        now_write=str(format(line_num,'6'))+' '+str(lines[index])+'\n'
        to_write.write(now_write)
        line_num+=1
    print('File',file_name,'has been written.',sep=' ')
    to_write.close()

def read_message():
    print('Enter rows of text. Quit by entering an empty row.')
    text = 's'
    row_list = []
    while text != '':
        text = input()
        if text != '':
            row_list.append(text)
    return row_list

main()