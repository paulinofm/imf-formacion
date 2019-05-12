# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:06:16 2019

@author: FERMASOLAR
"""

lista0 = [1,2,3,4,5,6]
objZip0 = zip(lista0)
for elemento in objZip0:
    print(elemento)
    print(elemento[0])

#unpacking lists   
print('LISTA DESEMPAQUETADA (1,2,3,4,5,6)')
n1 ,n2,*n = lista0
print('Segundo de la lista:' + str(n2))
print('resto final de la lista:' + str(n))

print('............................................................') 

lista = ([1,'a'],[2,'b'],[3,'c'],[4,'d'],[5,'e'],[6,'f'],[7,'g'])
objZip = zip(lista)

for elemento in objZip:
    print(elemento[0])
    
print('------------------------------------------------------------')    
    
lista1 = ('a','b','c','d','e')
lista2 = ('antonio','beatriz','carlos','diana','ernesto')
objZip2 = zip(lista1,lista2)

for elemento in objZip2:
    print(elemento)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')  

def ordenaporsegundo(elem):
    return elem[1]

listaA = [1,2,3,4,5]
listaB = (6,7,8,9,0)
objZip3 = zip(listaA,listaB)
listaZip3 = list(objZip3)
print(listaZip3)
listaZip3.sort(key = ordenaporsegundo)
print('LISTA ORDENADA POR SEGUNDO NUMERO:')
print(listaZip3)

for elemento in listaZip3:
    print(elemento)
    
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')  
conjunto = set(listaZip3)
print('conjunto con ' + str(len(conjunto)) + ' elementos')

for elemento in enumerate(conjunto):
    print(elemento)

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')  

Y = [[5,8,1,3],
    [6,7,4,7],
    [4,5,0,1],
    [3,6,8,2]]
print([list(Y_col) for Y_col in zip(*Y)])
print([list(zip(Y_col)) for Y_col in zip(*Y)])

print('oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')  

X = [[12,7],
    [4 ,5],
    [3 ,8]]
print('TRANSPUESTA DE LA MATRIZ [[12,7],[4 ,5],[3 ,8]]')
print([Y_col for Y_col in zip(*X)])