# cook your dish here
"""
Created on Mon Oct 21 03:32:41 2019

@author: Ritik
"""
def median(l):
    l.sort()
    return(l[1])
t=int(input())
for i in range(t):
    n=int(input())
    numbers=list(map(int,input().split()))
    while(len(numbers)>=3):
        m=median(numbers[:3])
        numbers.remove(m)
    print(*numbers)
