# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 22:10:18 2019

@author: s528218
"""

from itertools import permutations

perm = permutations('1234567890', 6)
count = 0
f = open("unused919.txt", "w+")
n=open("test1.txt","w+")
ucontinued = False
gcontinued = False

for i in set(perm):

    k = ",".join(i)
    k = k.replace(",", "")
    # print(k)

    if(not ucontinued and not gcontinued):
        u = input("Undergrad (u) or Grad (g) student:")
        if(u == 'u' and (int(k))%2 != 0):
            ucontinued = True
            continue
        elif(u == 'g' and (int(k))%2 != 1):
            gcontinued = True
            continue
        elif(u == 'q'):
            break
    elif(ucontinued):
        if((int(k))%2 != 0): continue
        else: ucontinued = False
    elif(gcontinued):
        if((int(k))%2 != 1): continue
        else: gcontinued = False
    d=dict()
    # print(k)
    r=input("Enter your name:")
    if(r == 'q'):
        break
    d[r]=k
    count+=1

    f.write(str(k)+"\n")
    for kp in sorted (d.keys()):
        n.write("%s:%s\n" % (kp, d[kp]))
        print("Your name and 919#: %s : %s" % (kp, d[kp]))

f.close()
n.close()



    
print("Amount of admissions",count)
