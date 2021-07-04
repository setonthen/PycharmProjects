def main():
    source_file=input('Enter the name of the file: ')
    try:
        file=open(source_file,'r')
        line_num=1
        for line in file:
            text=str(line.rstrip('\n'))
            print(str(format(line_num,'6'))+' '+text)
            line_num+=1
        file.close()
    except:
        print('There was an error in reading the file.')

main()
