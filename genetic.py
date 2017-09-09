#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 17:37:04 2017

@author: gramirez
"""
import numpy as np
import random as rd

#we create the actual fathers

father1 = [2,8,1,5,2,7,3,6]
father2 = [5,6,8,3,2,5,3,7]
father3 = [4,8,3,5,7,7,1,6]
father4 = [8,8,2,6,4,7,1,3]
#father4 = [1,6,2,5,7,4,0,3]
fathers = [father1,father2,father3,father4]

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
                   #print("posicion: ",i+1," valor: ",array[i])
                   #print("posicion: ",z+1," valor: ",array[z])
                   #print("")
        if array[i] == (array[z] + z - i):
              if i < z:
                   solution = solution + 2
                   #print("DS posicion: ",i+1," valor: ",array[i])
                   #print("DS posicion: ",z+1," valor: ",array[z])
                   #print("")
                   
    return (best_case - solution)/2


#partial checker
def partial_review(array,n):
    solution = 0
    size = np.size(array)
    best_case = size*(size-1)
    for i in range(0,n):
       for z in range(0,size):
        if array[i] == array[z]:
               if i < z:
                   solution = solution + 2
        if array[i] == (array[z] -(z -i)):
              if i < z:
                   solution = solution + 2
        if array[i] == (array[z] + z - i):
              if i < z:
                   solution = solution + 2
    return (best_case - solution)/2



def morph(array):
    answer = array
    answer[rd.randrange(0,8)] = rd.randrange(0,8)
    
    return answer
    
def check_all(array): #insert an array of fathers
    f_size = len(array)
    answer = [] #an array to contain an array with the next info [array,non-connected-queens]
    for i in range(0,f_size):
         temp = [array[i],review(array[i])]
         answer.append(temp)
    return sorted(answer,key=lambda order:order[1],reverse = True)

def mixing(array): #a sorted list of chances
    mixed = []
    #size = np.size(array,0)
    #length = np.size(array[:][:])
    #print(length)
    #cut_at = rd.randrange(1,length)
    temp = array[0][0][:3] + array[1][0][3:]
    temp = morph(temp)
    mixed.append(temp)
    temp = array[1][0][:3] + array[0][0][3:]
    temp = morph(temp)
    mixed.append(temp)
    temp = array[1][0][:5] + array[2][0][5:]
    temp = morph(temp)
    mixed.append(temp)
    temp = array[1][0][:5] + array[2][0][5:]
    temp = morph(temp)
    mixed.append(temp)
    mixed = check_all(mixed)
    print(mixed)
    return mixed 

def selection(array):
    #solution = 0
    #unsolved = True
    size = np.size(array)
    best_case = size*(size-1)
    actual_family = check_all(array) #we run first 
    print(actual_family)
    while(actual_family[0][1] < best_case):
          actual_family = mixing(actual_family)
          print(actual_family[0][1])
    print(actual_family)
    pass