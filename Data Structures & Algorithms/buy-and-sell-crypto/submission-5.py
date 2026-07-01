class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 0
        maxP = 0
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            maxP = max(maxP, prices[sell] - prices[buy])
            sell += 1
        return maxP