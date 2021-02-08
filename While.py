# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:28:06 2021

@author: Jorge
"""

while True:
    x=input("Ingrese el numero a contar: ")
    if x== 'q' or x == 'quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
        