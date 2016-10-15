
#############
### PENDU ###
#############

from donnees import *
import random
from fonction import *

player_name = name_player()
scores = find_score(player_name)
keep_playing = True

while keep_playing:
    print_score(scores,player_name)
    word_to_guess = dictionnaire[random.randrange(len(dictionnaire))]
    letters_list = create_stars(word_to_guess)
    win = False
    while not win and essais > 0:
        print_word(letters_list)
        letter = ask_letter()
        essais,letters_list = check_letter(essais,letters_list,word_to_guess,letter)
        win = check_win(letters_list, word_to_guess)
    keep_playing = play()
    update_scores(scores,essais,player_name)

final_print(win,player_name,word_to_guess,scores)


    
