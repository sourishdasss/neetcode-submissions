class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy_price = prices[0]
        buy = 0

        while buy < len(prices):
            if prices[buy] < min_buy_price:
                min_buy_price = prices[buy]
            curr_profit = prices[buy] - min_buy_price
            max_profit = max(curr_profit, max_profit)
            buy += 1

        return max_profit





        