# TIE-02100 Johdatus ohjelmointiin 
# Dancing Queen

def read_file(filename):
    
    # reads the played songs and their scores from the file

    try:
        fileobject = open(filename, "r")
        
        # TODO: initialize your data structure here
        single={}
        score_song={}

        # loop over fileobject row by row
        for row in fileobject:
            parts = row.strip().split(";")
            player = parts[0] # name of the player
            songs = parts[1:] # songs

            # TODO: make a data structure for this single
            #       player that includes his/her songs and scores
            single[player]=songs

            # loop over this player's songs
            for song in songs:
                parts = song.split(":")
                results = parts[1].split(",")
                name = parts[0] # name of the song
                # list of presses, all integer
                results = [int(elments) for elments in results]

                # TODO: connect these results to the song
                score_song[name]=results
            
            # TODO: add this player's data structure into the 
            #       main data structure
            single[player] = score_song
            score_song = {}
            
        return single # TODO return the main data structure

    except IOError:
        print("Error! The file could not be read.")
        return None


def main():

    coefficients = [5, 4, 2, 0, -6, -12]

    filename= input("Enter the name of the file: ")
    fileobject=open(filename,'r')
    name_score = read_file(filename)
    dic1={}
    dic2={}
    for row in fileobject:
        parts = row.strip().split(";")
        player = parts[0]  # name of the player
        songs = parts[1:]  # songs
        for song in songs:
            elements = song.split(":")
            name = elements[0]  # name of the song
            score_obtained=name_score[player][name]
            req=calculate(score_obtained)
            dic2[name]=req
        dic1[player] = dic2
        dic2={}
    arr_dic1=sorted(dic1)
    for x in range(len(dic1)):
        naam=arr_dic1[x]
        score=dic1[arr_dic1[x]]
        arr_dic2=sorted(score)
        print(naam+':')
        for y in range(len(arr_dic2)):
            aanka=score[arr_dic2[y]]
            geet=arr_dic2[y]
            print('- '+geet+': '+aanka+'%')


def calculate(list):
    sum_score=0
    for x in range(len(list)):
        sum_score+=list[x]
    max_score=sum_score*5
    scored=5*list[0]+4*list[1]+2*list[2]+0*list[3]-6*list[4]-12*list[5]
    ratio=format((scored/max_score)*100,'.2f')
    return ratio


main()
