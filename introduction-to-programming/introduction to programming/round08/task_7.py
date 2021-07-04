import os
def fix_filenames(folder):
    file = os.listdir(folder)
    file.sort()
    string = ''
    renamed_list = []
    try:
        for item in file:
            if item.endswith('.mp3'):
                line = item.strip('.mp3')
                list_line = line.split('-')
                if list_line[0].isdigit():
                    string = list_line[2] + '-' + list_line[1] + '.mp3'
                    path = os.path.join(folder,item)
                    new_path = os.path.join(folder,string)
                    os.rename(path,new_path)
                else:
                    pass
    except:
        pass