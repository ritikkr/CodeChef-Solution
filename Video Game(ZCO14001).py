# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:45:06 2019

@author: Ritik
"""
n,h=input().split()
n,h=int(n),int(h)
array=list(map(int,input().split()))
command=list(map(int,input().split()))
pos=0
value=0
for i in range(0,len(command)):
    if(command[i]==1):
        if(pos!=0):
            pos=pos-1
            
    if(command[i]==2):
        if(pos!=(n-1)):
            pos=pos+1
        
        
    if(command[i]==3): #pickup
        if(value==0): #crane k pass nhi h
            data=array[pos]
            if(data!=0):  #crane jis position p h us pos p value h ya  nhi
                array[pos]=array[pos]-1
                value=value+1
    
    if(command[i]==4):
        if(value!=0):
            if(array[pos]!=h):
                array[pos]=array[pos]+1
                value=value-1
            
    if(command[i]==0):
        break
print(*array)
