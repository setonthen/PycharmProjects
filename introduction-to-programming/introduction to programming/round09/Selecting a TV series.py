# TIE-02100 Johdatus ohjelmointiin


def read_file(filename):
    # reads and saves the series and their genres from the file

    try:
        ordered = []
        file = open(filename, "r")

        for row in file:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")
            for x in range(len(genres)):
                ordered.append(genres[x])
        managed = sorted(ordered)
        x = 0
        while x != len(managed) - 1:
            if managed[x] == managed[x + 1]:
                managed.remove(managed[x + 1])
            else:
                x += 1
        file.close()
        return managed


    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")
    names = read_file(filename)
    print('Available genres are: ', end='')
    for x in range(len(names)):
        if x != len(names) - 1:
            print(names[x], end=', ')
        else:
            print(names[x])
    while True:
        genre = input("> ")

        if genre == "exit":
            return

        file = open(filename, "r")
        series=[]
        for row in file:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")
            for x in range(len(genres)):
                if genre==genres[x]:
                    series.append(name)
        final=sorted(series)
        for element in range(len(final)):
            print(final[element])

main()
