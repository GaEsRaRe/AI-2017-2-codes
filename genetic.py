#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 17:37:04 2017

@author: gramirez
"""
import numpy as np

#we create the actual fathers

father1 = [2,8,1,5,2,7,3,6]
father2 = [5,6,8,3,2,5,3,7]
father3 = [4,8,3,5,7,7,1,6]
father4 = [8,8,2,6,4,7,1,3]

#let us get a number of pairs that don't collide based on an array

def review(array):
    solution = 0
    size = np.size(array)
    best_case = size*(size-1)
    for i in range(0,size):
       for z in range(0,size):
        if array[i] == array[z]:
               if i != z:
                   solution = solution + 1
                   #print("Recta posicion: ",i+1," valor: ",array[i])
                   #print("Recta posicion: ",z+1," valor: ",array[z])
        if array[i] == (array[z] -(z -i)):
              if i < z:
                   solution = solution + 2
                   print("posicion: ",i+1," valor: ",array[i])
                   print("posicion: ",z+1," valor: ",array[z])
                   print("")
        if array[i] == (array[z] + z - i):
              if i < z:
                   solution = solution + 2
                   #print("DS posicion: ",i+1," valor: ",array[i])
                   #print("DS posicion: ",z+1," valor: ",array[z])
                   #print("")
                   
    return (best_case-solution)/2
    