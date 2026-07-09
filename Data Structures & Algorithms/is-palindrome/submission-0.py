class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for c in s:
            if c.isalnum():
                new += c
            else:
                continue
        
        new = new.lower()

        l, r = 0, len(new) - 1

        while l < r:
            if new[l] != new[r]:
                return False
            l += 1
            r -= 1
        return True
            

        