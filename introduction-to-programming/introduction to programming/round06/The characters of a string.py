def main():
    test_string=(input('Enter a word: '))
    count=0
    space_count=0
    for ch in test_string:
        ch.lower()
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
            count+=1
        if ch==' ':
            space_count+=1
    vow_count=count
    consonant_count=len(test_string)-count-space_count
    print('The word',test_string,'contains',vow_count,'vowels and',
          consonant_count,'consonants')
main()