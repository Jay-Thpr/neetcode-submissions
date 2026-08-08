class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_profit = 0

        for p in prices:
            min_p = min(min_p, p)
            max_profit = max(max_profit, p - min_p)
        
        return max_profit