class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for word in strs:
            a = [0]*26
            for c in word:
                a[ord(c) - ord('a')] += 1
            hashmap[tuple(a)].append(word)
            
        

        return hashmap.values()

