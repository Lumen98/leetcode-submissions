from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        

        for num in nums:
            freq[num] += 1
        
        if freq.values() and max(freq.values()) > 1:
            return True
        else:
            return False