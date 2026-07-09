from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        # number : count
        res = []

        for i in range(k):
            max_number = max(count, key=count.get)
            res.append(max_number)
            del count[max_number]


        return res