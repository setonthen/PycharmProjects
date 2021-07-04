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

        if turns>4:
            turns=test(game,turns,mark)
        if turns==9:
            print("Draw!")


def print_dots(board):
    for col in range(3):
        for row in range(3):
            print(board[row][col], end='')
        print()

def first_player(cor_x,cor_y,b_list,sym):
        b_list[cor_x][cor_y]=sym
        print_dots(b_list)


def test(decide,rep,sym):
    for x in range(3):
        if decide[x][0] == decide[x][1] == decide[x][2]==sym:
            print('The game ended, the winner is ' + decide[x][0])
            return 10
        elif decide[0][x] == decide[1][x] == decide[2][x]==sym:
            print('The game ended, the winner is ' + decide[0][x])
            return 10
    if decide[2][0] == decide[1][1] == decide[0][2]==sym:
        print('The game ended, the winner is ' + decide[2][0])
        return 10
    elif decide[1][1] == decide[2][2] == decide[0][0]==sym:
        print('The game ended, the winner is ' + decide[0][0])
        return 10
    else:
        return rep

main()