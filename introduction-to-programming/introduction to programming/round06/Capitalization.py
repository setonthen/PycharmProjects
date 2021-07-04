def capitalize_initial_letters(letters):
    words=letters.split(' ')
    ready_words=''
    for x in range(len(words)):
        if x==len(words)-1:
            ready_words += words[x].capitalize()
        else:
            ready_words+=words[x].capitalize()+' '
    return ready_words
