"""
Created on Mon Oct 21 00:11:41 2019

@author: Ritik
"""
t=int(input())
if(t<1 or t>100):
    exit()
for i in range(t):
    n=int(input())
    if(n<7 or n>100):
        exit()
    
    numbers=list(map(int,input().split()))
    for i in numbers:
        if(i<350 or i>750):
            exit()
    count=1
    for i in range(1,n):
        if(i<=5):
            if(numbers[i]<min(numbers[:i])):
                count+=1
        if(i>5):
            if(numbers[i]<min(numbers[i-5:i])):
                count+=1
    print(count)
    
