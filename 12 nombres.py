# -*- coding: cp1252 -*-
# Programme inscrivant une suite de douze chiffre dont
# un terme est 3 fois sup�rieur au terme le pr�c�dant

a = 1               # variable de base
b = (a*3)**12       # variable servant � stopper � 12 termes
while a < b:        # condition
    a = a*3
    print a
