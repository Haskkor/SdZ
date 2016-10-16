# -*- coding: cp1252 -*-
# Programme inscrivant une suite de douze chiffre dont
# un terme est 3 fois supérieur au terme le précédant

a = 1               # variable de base
b = (a*3)**12       # variable servant à stopper à 12 termes
while a < b:        # condition
    a = a*3
    print a
