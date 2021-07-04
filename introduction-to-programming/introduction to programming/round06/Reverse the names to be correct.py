def reverse_name(name):
    last_name=''
    x=0
    while x<len(name):
        if name[x]!=',':
            last_name+=name[x]
            x+=1
        else:
            x=len(name)
    first_with_comma=name.strip(last_name)
    first_name=first_with_comma.strip(',')
    corr_last=last_name.strip()
    corr_first=first_name.strip()
    if corr_last=='' or corr_first=='':
        final=corr_first+corr_last
    else:
        final=corr_first+' '+corr_last
    return final

