class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        elif len(s) < 2:
            return 1
        
        window = set()
        
        l, r = 0, 0

        res = 1

        while l < len(s) and r < len(s):
            while s[r] in window and l < r and r < len(s):
                window.remove(s[l])
                l += 1
                
            window.add(s[r])
            res = max(len(window), res)
            r += 1






        return res

