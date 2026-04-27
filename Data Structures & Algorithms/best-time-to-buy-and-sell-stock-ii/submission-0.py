class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = False
        profit = 0
        for i in range(len(prices)-1):
            if stock and prices[i]>prices[i+1]:
                profit += prices[i]
                stock = False
            if not stock and prices[i]<prices[i+1]:
                profit -= prices[i]
                stock = True
        if stock:
            profit += prices[-1]
        return profit

        