# TIE-02100 Johdatus ohjelmointiin

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    while True:

        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            
            word=input("Enter the word to be translated: ")
            if word in english_spanish:
                print(word,"in Spanish is",english_spanish[word],sep=' ')
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            word_english=input("Give the word to be added in English: ")
            word_spanish=input("Give the word to be added in Spanish: ")
            english_spanish[word_english]=word_spanish

        elif command == "R":
            word=input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else:
                print("The word", word,
                      "could not be found from the dictionary.")

        elif command== 'P':
            for word, translation in sorted(english_spanish.items()):
                print(word,translation,sep=' ')

        elif command=='T':
            words=input('Enter the text to be translated in Spanish: ')
            word_list=words.split()
            for x in range(len(word_list)):
                if word_list[x] in english_spanish:
                    word_list[x]=english_spanish[word_list[x]]
            print('The text, translated by the dictionary: ')
            for y in range(len(word_list)):
                print(word_list[y],end=' ')
            print()
        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


main()
