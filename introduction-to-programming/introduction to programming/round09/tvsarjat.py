# TIE-02100 Johdatus ohjelmointiin


def read_file(filename):
    # reads and saves the series and their genres from the file

    # TODO initialize a new data structure

    try:
        file = open(filename, "r")

        for row in file:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")

            # TODO add the info to the data structure

        file.close()
        return  # TODO return the data structure

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():

    filename = input("Enter the name of the file: ")
    TODO = read_file(filename)

    # TODO print the genres

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        # TODO print the series ...

main()
