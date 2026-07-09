class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) is not len(t):
            return False
        s = list(s)
        t = list(t)

        s.sort()
        t.sort()

        for i in range(0,len(s)):
            if s[i] == t[i]:
                continue
            else:
                return False
        
        return True
        

            