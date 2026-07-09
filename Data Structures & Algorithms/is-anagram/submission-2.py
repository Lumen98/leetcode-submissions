class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        hashmap2 = {}

        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
        
        for j in range(len(t)):
            if t[j] in hashmap2:
                hashmap2[t[j]] += 1
            else:
                hashmap2[t[j]] = 1
        
        return hashmap2 == hashmap

        

            