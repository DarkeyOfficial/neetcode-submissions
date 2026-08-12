class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1     # left = buy / right = sell
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:           # profitable
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:                               # not profitable
                l = r
            r += 1
        
        return maxP