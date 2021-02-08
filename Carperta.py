# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:22:30 2021

@author: USUARIO
"""
lista=[]
file=open('devices.txt')
for a in file:
    a=a.strip()
    lista.append(a)
    print(a)
file.close()
print(lista)