# -*- coding: cp1252 -*-
# Programme convertissant une nombre de secondes donn�es en
# nombre d'ann�es, de mois, de semaines, de jours, d'heures, de minutes,
# et de secondes.

X = 60000000               # nombre de secondes donn�es
S = 1                      # secondes
M = 60 * S                 # minutes
H = 60 * M                 # heures
J = 24 * H                 # jours
F = 7 * J                  # semaines
K = 4 * F                  # mois          
A = 12 * K                 # ann�e  
print A, "secondes dans l'ann�e"
print K, "secondes dans le mois"
print F, "secondes dans la semaine"
print J, "secondes dans la journ�e"
print H, "secondes dans l'heure"
print M, "secondes dans la minute"
print (60000000 % S) , "modulo des 60M par les secondes"
print (60000000 % 60), "modulo des 60M par les minutes"
print (60000000 % 60 * 60), "modulo des 60M par les heures"
print (60000000 % 60 * 60 * 24), "modulo des 60M par les jours"
print (60000000 % 60 * 60 * 24 * 7), "modulo des 60M par les semaines"
print (60000000 % 60 * 60 * 24 * 7 *4), "modulo des 60M par les mois"
print (60000000 % 60 * 60 * 24 * 7 * 4 * 12), "modulo des 60M par les ann�es"
print (60000000 / 1), "secondes dans 60M de secondes"
print (60000000 / 60), "minutes dans 60M de secondes"
print (60000000 / 60 / 60), "heures dans 60M de secondes"
print (60000000 / 60 / 60 / 24), "jours dans 60M de secondes"
print (60000000 / 60 / 60 / 24 / 7), "semaines dans 60M de secondes"
print (60000000 / 60 / 60 / 24 / 7 / 4), "mois dans 60M de secondes"
print (60000000 / 60 / 60 / 24 / 7 / 4 / 12), "ans dans 60M de secondes"


