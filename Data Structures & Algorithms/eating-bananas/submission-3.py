class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if len(piles) == h:
            return max(piles)
        
        # run a binary search on k

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            
            hours = 0

            for i in range(len(piles)):
                hours += math.ceil(piles[i] / k)

            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
    
        return res


        
