# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:34:08 2021

@author: Jorge
"""

file=open('devices.txt','a')
while True:
    Dat=input("Ingrese nuevo datos: ")
    if Dat== 's' or Dat == 'salir':
        print('Todo salio bien')
        break
    file.write(Dat +"\n")
file.close()
