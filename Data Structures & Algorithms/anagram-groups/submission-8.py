from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for word in strs:
            a = [0] * 26

            for c in word:
                index = ord(c) - ord('a')

                a[index] += 1
            
            hashmap[tuple(a)].append(word)
        
        return list(hashmap.values())
        

            
