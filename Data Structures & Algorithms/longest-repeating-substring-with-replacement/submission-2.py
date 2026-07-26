from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        

        hashmap = defaultdict(int) # letter : freq in our current window

        l = 0

        maxFreq = 0
        res = 0
        # A A B B
        # 0 1 2 3
        for r in range(len(s)):
            hashmap[s[r]] += 1
            maxFreq = max(maxFreq, hashmap[s[r]])

            while (r - l + 1) - maxFreq > k: 
                hashmap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res

