#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d_m={}
        for i in magazine:
            d_m[i]=d_m.get(i,0)+1
        d_r={}
        for i in ransomNote:
            d_r[i]=d_r.get(i,0)+1
            
        arr=[] #Initializing an array
        for i in d_r:
            if i in d_m: #Checking if it is present in d_m
                if d_r[i]>d_m[i]:

                    arr.append(-1) #Appending -1 if we come across an element whose count in ransomNote is more than magazine
                else:
                    
                    arr.append(1) #Appending 1 if we come across an element whose count in ransomNote is less than magazine
            else: #If it isn't present in d_m
                
                arr.append(-1)
       
    #If all elements in arr are equal to one, it implies that count of each element
    # in ransomNote is less than magazine; hence ransomNote can be constructed from magazine
        if arr.count(1)==len(arr): 
            return True
        else:
            return False

