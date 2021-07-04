import os
from os import rename
from os import listdir
def fix_filenames(folder_name):
    file = listdir(folder_name)
    file.sort()
    try:
        string = ''
        for item in file:
            if item.endswith('.mp3'):
                line = item.strip('.mp3')
                list_line = line.split('-')
                if list_line[0].isdigit():
                    string = list_line[2] + '-' + list_line[1] + '.mp3'
                    path = os.path.join(folder_name,item)
                    new_path = os.path.join(folder_name,string)
                    rename(path,new_path)
                else:
                    pass
    except:
        pass