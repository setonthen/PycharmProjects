# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: ristinolla, program code template
# Mukesh Aryal, 268456

def main():

    # TODO: implement the datastructure for storing the board
    game = [['.', '.', '.'],['.','.','.'],['.','.','.']]
    print_dots(game)
    turns = 0  # How many turns have been played

    # The game continues until the board is full.
    # 9 marks have been placed on the board when the player has been
    # switched 8 times.
    while turns < 9:

        # Change the mark for the player
        if turns % 2 == 0:
            mark = "X"
        else:
            mark = "O"
        coordinates = input("Player " + mark + ", give coordinates: ")

        try:
            x, y = coordinates.split(" ")
            x = int(x)
            y = int(y)

            # TODO: implement the turn of one player here
            if game[x][y]!='X' and game[x][y]!='O':
                first_player(x,y,game,mark)
                turns+=1
            else:
                print('Error: a mark has already been placed on this square.')
                turns=turns
        except ValueError:
            print("Error: enter two integers, separated with spaces.")

        except IndexError:
            print("Error: coordinates must be between 0 and 2.")




def print_dots(board):
    for col in range(3):
        for row in range(3):
            print(board[row][col], end='')
        print()

def first_player(cor_x,cor_y,b_list,sym):
        b_list[cor_x][cor_y]=sym
        print_dots(b_list)

main()
