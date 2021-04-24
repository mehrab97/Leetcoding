#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_nums=sum(nums) #The sum of the entire list
        running_sum=nums[0]#Initializing sum_nums to be the first element of nums

        #Going till the second last element
        for i in range(len(nums)-1):
            nums[i]=running_sum
            running_sum+=nums[i+1]
        #Replacing the last element with sum of the original array nums
        nums[len(nums)-1]=sum_nums
        return nums

