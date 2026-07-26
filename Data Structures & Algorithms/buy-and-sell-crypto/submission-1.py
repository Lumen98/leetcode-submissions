class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        maxProfit = 0

        currMin = prices[0]

        for i in range(1, len(prices)):
            currProfit = prices[i] - currMin
            
            if prices[i] < currMin:
                currMin = prices[i]

            maxProfit = max(maxProfit, currProfit)

        return maxProfit

            

