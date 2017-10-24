# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:41:27 2017

@author: diego
"""

# 1 test  
import string
    
def firstDuplicate(a):
    oldies={}
    notfound=True
    for i in range(len(a)):
        try:
            if oldies[a[i]]==a[i]:
                notfound=False
                return a[i]     
        except:
            oldies[a[i]]=a[i]
    if notfound:
        return -1        


# 2 test    
import math    
    
def firstNotRepeatingCharacter(s):
    letters=list(set(s))
   # print(letters)
    d={}
    b={}        
    for i in letters:
        d[i]=i
        b[i]=i       
    for i in range(len(s)):   
        try:    
            try:
                del d[s[i]]
            except:
                del b[s[i]]
        except:
            pass    
    #print(b,d)    
    if len(b)==0:
        return '_'       
    else:
        mini=math.inf
        #print(b)
        for i in letters:
            try:
                if s.index(b[i])<mini:
                    mini=s.index(b[i])
                    first_one=b[i]
            except:
                pass
        return first_one

# 3 test
def rot4(a,i,j):
    n=len(a) 
    b=a[i][j]
    c=0
    for k in range(4):
        c=b
        old_i=i
        old_j=j
        i=old_j
        j=n-old_i-1
        b=a[i][j]
        a[i][j]=c
    return a
    
def rotateImage(a):
    if len(a)>3:  
        for j in range(len(a)-3+1):
            for i in range(j,len(a)-1-j):
                print(j,i)
                a=rot4(a,j,i)
    else:
         for j in range(len(a)-1):
             a=rot4(a,0,j)
    return a   


# 4 test

def slice_2d(grid,x_in,x_end,y_in,y_end):
    return [grid[i][x_in:x_end] for i in range(y_in,y_end)]  

def check_rows(grid):
    good=True
    for i in range(9):
        rows=list((''.join(grid[i])).replace(".",""))
        if len(set(rows))!=len(rows):
            good=False
            break
    return good

def check_columns(grid):
    good=True
    for i in range(9):
        column=list((''.join([row[i] for row in grid]  )).replace(".",""))
        if len(set(column))!=len(column):
            good=False
            break
    return good     

def check_sections(grid):
    good = True
    for i,j in [(0,3),(3,6),(6,9)]:
        for n,m in [(0,3),(3,6),(6,9)]:
            sliced2d=slice_2d(grid,i,j,n,m)
            l=sum(sliced2d, [])
            section=list((''.join(l)).replace(".",""))
            if len(set(section))!=len(section):
                good=False
                break
    return good            
            
def sudoku2(grid):
    if check_rows(grid) and check_columns(grid) and check_sections(grid):
        return True
    else:
        return False







    
