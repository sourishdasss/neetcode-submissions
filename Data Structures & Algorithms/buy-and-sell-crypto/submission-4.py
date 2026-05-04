class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = [101] * n

        min_price[0] = prices[0]
        for i in range(1, len(min_price)):
            min_price[i] = min(min_price[i-1], prices[i])
        
        max_profit = 0
        # populate max profit array
        for i in range(1, len(min_price)):
            max_profit = max(max_profit, prices[i] - min_price[i])
        
        return max_profit