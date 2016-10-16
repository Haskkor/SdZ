# -*- coding: cp1252 -*-
# programme permettant la conversion de l'euro en dollar
# sur une base de 1 euro = 1.65 dollar et allant jusqu'a 16384 euros

a, b = 1, 1.65            # variable pour l'euro et le dollar
while a < 16384:          # condition
    a, b = a*2, b*2       
    print a,b
