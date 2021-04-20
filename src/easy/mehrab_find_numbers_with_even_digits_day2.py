#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            return len([ele for ele in nums if len(str(ele))%2==0])

# Go through each element of the list and use list comprehension to return a list such that length of each string 
# element in nums is a multiple of 2. 


# In[ ]:




