
##########################
### FONCTIONS DU PENDU ###
##########################

import pickle
import donnees
import os

# Lis le score du joueur dans le fichier de sauvegarde, retourne un score
# nul si le joueur n'existe pas

def find_score(player_name):
    if os.path.exists(donnees.file_name):
        file = open(donnees.file_name,"rb")
        pickler = pickle.Unpickler(file)
        score = pickler.load()
        file.close()
    else:
        score = {}
        score[player_name] = 0
    return score

# Affiche le score du joueur

def print_score(scores,player_name):
    if player_name in scores:
        print("Vous avez {} points.".format(scores[player_name]))
    else:
        print("Vous avez 0 point.")

# Demande du nom du joueur

def name_player():
    player_name = input("Entrez un nom de joueur : ")
    while player_name == "":
        player_name = input("Entrez un nom de joueur : ")
    print("")
    return player_name

# Demande une lettre au joueur

def ask_letter():
    letter = input("Lettre à jouer : ")
    while not letter.isalpha() and len(letter) > 1:
        letter = input("Lettre à jouer : ")
    return letter

# Création d'une liste d'étoiles

def create_stars(word):
    star_list = []
    for lettre in word:
        star_list.append("*")
    return star_list

# Vérification de la lettre envoyée
# Modification de la liste d'étoiles et du nombre d'essais

def check_letter(tries,letters_list,word,letter):
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                letters_list[i] = letter
        print("Bravo ! ")
    else:
        tries -= 1
        print("Essayez encore !")
    print("")
    return tries,letters_list

# Affichage de la liste de lettre devinées

def print_word(letters_list):
    print("Mot à deviner : ")
    for letter in letters_list:
        print(letter,end=' ')
    print("")

# Contrôle la victoire

def check_win(letters_list, word_to_guess):
    word = "".join(letters_list)
    if word == word_to_guess:
        return True
    else:
        return False

# Demande au joueur si il veut continuer la partie

def play():
    keep_playing = input("Voulez-vous continer à jouer O/N : ")
    while keep_playing.lower() != "o" or keep_playing.lower() != "o":
        keep_playing = input("Voulez-vous continer à jouer O/N : ")
    if keep_playing.lower() == "o":
        return True
    else:
        return False

# Met à jour les scores et les enregistre

def update_scores(scores,essais,player_name):
    scores[player_name] += essais
    file = open(donnees.file_name,"wb")
    pickler = pickle.Pickler(file)
    pickler.dump(scores)

# Affichage final

def final_print(win,player_name,word_to_guess,scores):
    if win:
        print("Bravo {} ! Le mot était bien : {}. Vous avez maintenant {} points.".format(player_name,word_to_guess,scores[player_name]))
    else:
        print("Dommage {} ! Le mot était : {}. Vous avez {} points.".format(player_name,word_to_guess,scores[player_name]))

# Contrôle
