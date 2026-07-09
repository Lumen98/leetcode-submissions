class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        

        hashmap = {}
        hashmap2 = {}

        for c in range(0,len(s)):
            hashmap[ord(s[c]) - ord('a')] = hashmap.get(ord(s[c]) - ord('a'), 0) + 1

        for i in range(0,len(t)):
            hashmap2[ord(t[i]) - ord('a')] = hashmap2.get(ord(t[i]) - ord('a'), 0) + 1


        if hashmap == hashmap2:
            return True
        else:
            return False




        