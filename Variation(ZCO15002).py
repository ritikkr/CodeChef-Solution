# cook your dish here
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 04:11:47 2019

@author: Ritik
"""

n,k=input().split()
n,k=int(n),int(k)
numbers=list(map(int,input().split()))
count=0
for i in range(len(numbers)):
    for j in range(i,len(numbers)):
        if(i!=j):
            if(abs(numbers[i]-numbers[j])>=k):
                count+=1
print(count)
