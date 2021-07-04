def read_file(file_name):
    file=open(file_name,'r')
    info={}
    personal_info={}
    for line in file:
        stripped=line.rstrip('\n')
        detail=stripped.split(';')
        info['name']=detail[1]
        info['phone']=detail[2]
        info['email']=detail[3]
        if len(detail)==5:
            info['skype']=detail[4]
        personal_info[detail[0]]=info
        info={}
    return personal_info

