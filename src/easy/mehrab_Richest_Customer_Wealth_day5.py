#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum=sum(accounts[0]) #Initializing the max sum to be the sum of elements of first sub_array


    #Going through each sub-array of accounts 2-D list
        for i in range(len(accounts)):
            if sum(accounts[i])>max_sum: #If sum of elements of sub-array > max_sum, replace max_sum with this
                max_sum=sum(accounts[i])
        return max_sum #Finally return the max_sum
    

