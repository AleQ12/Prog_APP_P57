# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:11:57 2021

@author: Jorge
"""

acl=int(input("ingrese el # de ACL:"))
if acl>=1 and acl<=99:
    print('La ACl es Estandar')
elif acl>=100 and acl<=199:
    print('La ACL es Extendida')
else:
    print("El numero ingresado no es de un ACl")