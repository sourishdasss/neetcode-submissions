class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0

        while buy < len(prices) - 1:
            sell = buy + 1
            while sell < len(prices):
                tmp_profit = prices[sell] - prices[buy]
                max_profit = max(tmp_profit, max_profit)
                sell += 1
            buy += 1

        return max_profit
        