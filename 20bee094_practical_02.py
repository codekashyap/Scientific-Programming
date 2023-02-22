#!/usr/bin/env python
# coding: utf-8

# # 1. Write a function that takes a string as a parameter and returns a string with
#     every successive repetitive character replaced with a star(*). For Example,
#     ‘balloon’ is returned as ‘bal*o*n’.

# In[31]:



def sol(str):
    l=[]
    for i in range(0,len(str)):
        l.append(str[i])
    for j in range(0,len(l)):
        if l[j] in l[ :j ]:
            l[j] = "*" 
    st="".join(l)        
    return st   


a="balloon"
print(sol(a))

    
            
               


# # 2. Write a function that takes a number as n input parameter and returns the
#   corresponding text in words; for example, on input 452, the function should
#   return ‘Four Five Two’. Use an indexed list for mapping to digits to their string
#   representation.

# In[43]:


def sol(list):
    d={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    k=[]
    for i in list:
        k.append(d[i])
    return k
inp = list(map(int,input().split(" ")))
print(sol(inp))


# # 3. Write a recursive function that takes x value as an input parameter and print x-
#     digit strictly in increasing number. [i.e. x = 6 than output 67891011]

# In[14]:


def rec(a,b):
    if b < a*2: 
        print(b,end = " ")
        return rec(a,b+1)
    else:
        return
  
a=int(input())
print(rec(a,a))
    
    
    


# In[ ]:





# In[ ]:




