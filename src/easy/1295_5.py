import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ev_d_count = 0
        for i in nums:
            if i != 0:
                if math.floor(math.log10(i)) % 2 == 1:
                    ev_d_count += 1
        return ev_d_count