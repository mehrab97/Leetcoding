#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for i in stones:
            if i in jewels:
                count+=1
        return count
#Take a counter, iterate through each character in stones, if it's present in jewels increment the count. It's given 
# that each character of jewels is unique so we don't require to iterate through jewels in this case and just need
# to check if each character in stones is present in jewels or not

