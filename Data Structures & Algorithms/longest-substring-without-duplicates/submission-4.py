class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: 
            return 0
        if len(s) == 1:
            return 1

        window = set()

        l, r = 0, 0

        res = 0

        while l < len(s) and r < len(s):
            if s[r] not in window:
                window.add(s[r])
                r += 1
            else:
                while l < r and s[r] in window:
                    window.remove(s[l])
                    l += 1
                window.add(s[r])
                r += 1

            res = max(res, len(window))

        return res











