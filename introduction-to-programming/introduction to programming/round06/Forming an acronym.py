def create_an_acronym(text):
    full_words=text.split(' ')
    acronym=''
    for x in range(len(full_words)):
        acronym+=full_words[x][0]
    return acronym.upper()
