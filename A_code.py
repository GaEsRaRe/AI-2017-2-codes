# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 20:31:59 2017

@author: Gabriel PC
"""

#A* blind proyect

import numpy as np


class node: #Easy to mod node
    id_number = 0
    data = ""
    pass

class graph:
    data = [] #includes every node
    mapping = [] #include of paths
    entropy = [] # (a,e,lenght) is a basic lineal distance between two points given as data
    
    def define_entropy(self,array): #Let us add an entropy mapping
        self.entropy = array
        pass
    
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
        temp = [a,b,size]
        self.mapping.append(temp)

    def pathfinding(self,a,b):
        entry = []
        visited = []
        path_finded = False
        while path_finded == False:
            None #temp data
    pass



