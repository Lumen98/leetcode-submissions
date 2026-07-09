class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        

        hashmap = {}

        for c in range(0,len(s)):
            hashmap[ord(s[c]) - ord('a')] = hashmap.get(ord(s[c]) - ord('a'), 0) + 1

        for i in range(0,len(t)):
            hashmap[ord(t[i]) - ord('a')] = hashmap.get(ord(t[i]) - ord('a'), 0) - 1

        for count in hashmap.values():

            if count != 0:
                return False
        
        return True




        