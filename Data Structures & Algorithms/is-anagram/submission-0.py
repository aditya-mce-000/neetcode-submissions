from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = Counter(s)
        count1 = dict(sorted(count1.items()))
        count2 = Counter(t)
        count2 = dict(sorted(count2.items()))
        if count1 == count2:
            return True
        return False