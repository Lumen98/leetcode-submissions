from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count2 = Counter(s1)

        def isPermutation(curr):
            count1 = Counter(curr)
            if count1 == count2:
                return True
            return False

        len1 = len(s1)
        len2 = len(s2)

        l, r = 0, len1 - 1

        while l <= r and r < len2: 
            curr = s2[l:r + 1]
            print(curr)
            if isPermutation(curr): 
                return True
            
            l += 1
            r += 1

        return False






