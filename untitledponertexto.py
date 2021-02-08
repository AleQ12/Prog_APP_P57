# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:19:54 2021

@author: USUARIO
"""

file=open('devices.txt','a')
while True:
    n = input('Ingrese un nuevo Iten:')
    if n == 'exit':
        print('LISTO !!')
        break
    else:
        file.write(n + '\n')
      
file.close()