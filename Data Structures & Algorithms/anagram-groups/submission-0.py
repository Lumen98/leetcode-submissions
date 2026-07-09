class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            a = [0]*26
            for c in s:
                a[ord(c) - ord('a')] += 1
            hashmap[tuple(a)].append(s)
        return hashmap.values() 





    


        


        
