class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for word in strs:
            arr = [0]*26
            for c in word:
                arr[ord(c) - ord('a')] += 1
            hashmap[tuple(arr)].append(word)

        return hashmap.values()