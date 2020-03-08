# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 10:01:25 2019

@author: s526521
"""

f = open("unused919.txt", "w+")
#f = open("unused919.txt", "r")
#print("File created")


for i in range (720):
    
    f.write(str(i+1)+"\n")
    print(str(i+1))
    
#f1 = f.readlines()
#print(f1[1])
#for x in f1:
#    print(x)

f.close()