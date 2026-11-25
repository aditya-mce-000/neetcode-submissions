from collections import Counter

class Solution:
    def hasDuplicate(self, nums):
        count = Counter(nums)
        for i in range(len(nums)):
            if (count[nums[i]])>1:
                return True        
        return False