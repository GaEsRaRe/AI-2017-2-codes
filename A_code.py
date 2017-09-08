# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 20:31:59 2017

@author: Gabriel PC
"""

#A* blind project
#language: Python 3.x


import numpy as np


class node: #Easy to mod node
    id_number = 0
    data = ""
    pass

class graph:
    data = [] #includes every node
    mapping = [] #include of paths
    heuristic = [] # (a,e,lenght) is a basic lineal distance between two points given as data
    
    def define_heuristic(self,array): #Let us add an heuristic mapping
        self.heuristic = array
        pass
    
    def get_heuristic(self, x,y):
        answer = 9999 #in case there's no possible way to reach
        for i in range(0,np.size(self.heuristic)):
            if self.heuristic[i][0] == x and self.heuristic[i][1] == y:
                answer = heuristic[i][2]
        
        return answer 
    
    def add(self,x):
        self.data.append(x)
        pass
    
    def check(self,a,b): #check if the path is possible
        testing = False
        t1,t2 = False, False
        for i in range(0,np.size(self.data)):
            if self.data[i] == a:
                t1 = True
            if self.data[i] == b:
                t2 = True
        if t1 == True and t2 == True:
            testing = True
        if a == b:
            testing = False
        return testing
    
    def knot(self,a,b,size): #add a path between two nodes
        valid = self.check(a,b)
        if valid == False:
            print("Don't exist")
            pass
        temp = [a,b,size,0] #first, second, lenght, non-visited
        self.mapping.append(temp)

    def exist(self,array,x):
        answer = False
        for i in range(0,np.size(array)):
            if array[i] == x:
                answer = True          
        return answer
    
    def pathfinding(self,a,b):
        father = 0;
        first = [a,self.get_heuristic(a,b),father] #id, cost, id_father
        entry = [a]
        visited = []
        path_finded = False
        while path_finded == False:
            for i in range(0, np.size(self.heuristic)):
                if self.heuristic[i][0] == a:
                    temp = self.exist(visited,a)
                    if temp == False:
                        cost = self.get_heuristic(a,b) + father
                        data = [self.heuristic[i][1], cost, self.heuristic[i][0]]
    pass



