your_score=int(input('How do you feel? (1-10) '))
good_vibe=7
if your_score<1 or your_score>10:
    print('Bad input!')
elif your_score==10:
    print('A suitable smiley would be :-D')
elif your_score>good_vibe:
    print('A suitable smiley would be :-)')
elif your_score==1:
    print('A suitable smiley would be :\'(')
elif (your_score<4):
    print('A suitable smiley would be :-(')
else:
    print('A suitable smiley would be :-|')
