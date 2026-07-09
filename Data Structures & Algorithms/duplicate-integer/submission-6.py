class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)

        if freq.values() and max(freq.values()) > 1:
            return True
        else:
            return False

        