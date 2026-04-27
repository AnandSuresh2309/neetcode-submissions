class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min,profit = prices[0],0
        for i in range(1,len(prices)):
            if prices[i] > min:
                profit = max(profit, prices[i] - min)
            elif prices[i] < min:
                min = prices[i]
        return profit
