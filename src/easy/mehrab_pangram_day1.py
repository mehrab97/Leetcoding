#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        #Initializing a list
        arr=[]
        
        #Appending all elements of sentence string to list 'arr'
        for i in sentence:
            arr.append(i)
            
        #set(arr) will give all unique elements and since there are 26 alphabets, 
        #we need to check the occurrence atleast once
        if len(set(arr))==26:
            return True
        else:
            return False

