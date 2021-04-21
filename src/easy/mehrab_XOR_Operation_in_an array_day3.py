#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        #Defining the nums array
        nums=[int(start+2*i) for i in range (n)]
        
        #Initializing the xor
        xor=nums[0]
        
        for i in range(1,len(nums)):
            xor^=nums[i] #Taking bitwise xor of each element
        return xor

