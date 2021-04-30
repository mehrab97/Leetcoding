#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={} #Initializing dictionary

        for i in nums: #Creating key, value pairs
            d[i]=d.get(i,0)+1
            
        for i in d: #Going through the dictionary
            if d[i]>len(nums)//2: #If the occurrence of the key is more than ⌊n / 2⌋ times, return that key
                return i

