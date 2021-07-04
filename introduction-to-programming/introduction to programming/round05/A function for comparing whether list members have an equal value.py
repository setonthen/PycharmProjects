def are_all_members_same(check_list):
    index=0
    while index<len(check_list):
        if check_list[0]==check_list[index]:
            index+=1
        else:
            index=len(check_list)+1
    if index==len(check_list):
        return True
    else:
        return False



