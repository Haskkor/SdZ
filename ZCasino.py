# -*- coding :Latin -1 -*

import os,math,random

def askMoney():
        money = -1
        while money < 0:
                money = input("Entrez une somme de départ : ")
                try:
                        money = int(money)
                        if money < 0:
                                print("La somme ne peut pas être négative.")
                except ValueError:
                        print("Vous n'avez pas saisi un nombre.")
                        money = -1
                        continue
        return money

def askNumber():
        number = -1
        while number < 0 or number > 50:
                number = input("Entrez un numéro entre 0 et 50 : ")
                try:
                        number = int(number)
                        if number < 0 or number > 50:
                                print("Le numéro n'est pas compris entre 0 et 50.")
                except ValueError:
                        print("Vous n'avez pas saisi un nombre.")
                        number = -1
                        continue
        return number

def askSum():
        summ = -1
        while summ < 0:
                summ = input("Entrez une somme à miser : ")
                try:
                        summ = int(summ)
                        if summ < 0:
                                print("La somme ne peut pas être négative.")
                except ValueError:
                        print("Vous n'avez pas saisi un nombre.")
                        summ = -1
                        continue
        return summ

def marbleRoll():
	return random.randrange(50)

def gainLoss(marble,number,summ):
        if number == marble:
                print("Vous avez gagné : ", summ * 3)
                return summ * 3
        elif marble % 2 == 0 and number % 2 == 0 or marble % 2 == 1 and number % 2 == 1:
                print("Vous avez gagné : ", math.ceil(summ / 2))
                return math.ceil(summ / 2)
        else:
                print("Vous avez perdu.")
                return -summ

def keepPlaying():
        answer = input("Voulez-vous continuer à jouer (O/N) : ")
        if answer == "O":
                return True
        elif answer == "N":
                return False
        else:
                print("Réponse invalide.")
                keepPlaying()

def mainProg():
        money = askMoney()
        run = True

        while run and money > 0:
                number = askNumber()
                summ = askSum()
                marble = marbleRoll()
                print("Le croupier a tiré le numéro : ", marble)
                money += gainLoss(marble,number,summ)
                print("Votre total d'argent est maintenant de : ", money)
                if money <= 0:
                        print("Vous n'avez plus d'argent.")
                        run = False
                else:
                        run = keepPlaying()        

mainProg()

os.system("pause")
