# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 17:12:13 2021

@author: HOME
"""

from random import randrange


print('TOSS TIME!!')

toss=randrange(0,2,1)
if toss==0:
    sys_toss="Tail"
else:
    sys_toss="Head"
    
my_toss=input('what you want Head or Tail: ')

totals=[]

if sys_toss==my_toss:
    print('User Won the Toss and Choose to BAT first.')
    machine=randrange(1,7,1)
    for i in range(1,3,1):
        total1=total2=0
        if i==1:
            print("1st inning")
            while True:
                me=int(input())
                if me>6:
                    print("no run")
                if machine==me:
                    print("out!")
                    print("total =",total1)
                    totals.append(total1)
                    print("target =",total1+1)
                    break
                else:
                    if not me>6:
                        total1+=me
                    
        else:
            print("2nd inning")
            while total2<=totals[0]:
                me=int(input())
                if me>6:
                    print("no run")
                if machine==me:
                    print("out!")
                    print("total =",total2)
                    totals.append(total2)
                    break
                else:
                    if not me>6:
                        total2+=me
            totals.append(total2)
                    
    if totals[0]>totals[1]:
        print("user won the match")
    elif totals[0]==totals[1]:
        print("draw!")
    else:
        print("total =",total2)
        print("machine won the match")
              
        
        
else:
    print('Machine Won the Toss and Choose to BAT First.')
    machine=randrange(1,7,1)
    for i in range(1,3,1):
        total1=total2=0
        if i==1:
            print("1st inning")
            while True:
                me=int(input())
                if me>6:
                    print("no run")
                if machine==me:
                    print("out!")
                    print("total =",total1)
                    totals.append(total1)
                    print("target =",total1+1)
                    break
                else:
                    if not me>6:
                        total1+=me
                    
        else:
            print("2nd inning")
            while total2<=totals[0]:
                me=int(input())
                if me>6:
                    print("no run")
                if machine==me:
                    print("out!")
                    print("total =",total2)
                    totals.append(total2)
                    break
                else:
                    if not me>6:
                        total2+=me
            totals.append(total2)
                    
    if totals[0]>totals[1]:
        print("machine won the match")
    elif totals[0]==totals[1]:
        print("draw!")
    else:
        print("total =",total2)
        print("user won the match")
        

totals.clear()
print(totals)




















     