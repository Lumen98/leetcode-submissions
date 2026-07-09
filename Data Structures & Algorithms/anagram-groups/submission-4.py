from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        # k=the total ascii value of the word
        # v= the word
        for word in strs:
            key = "".join(sorted(word))
            hashmap[key].append(word)
    

        return list(hashmap.values())