from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for i in range(len(strs)):
            arr = [0] * 26

            for c in strs[i]:
                arr[ord(c) - ord('a')] += 1
            
            hashmap[tuple(arr)].append(strs[i])

        return list(hashmap.values())




















