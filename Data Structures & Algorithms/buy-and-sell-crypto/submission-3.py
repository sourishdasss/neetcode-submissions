class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min_buy = 101
        buy_prices = []

        for p in prices:
            curr_min_buy = min(curr_min_buy, p)
            buy_prices.append(curr_min_buy)

        print(buy_prices)

        max_profit = 0

        i = 0

        while i < len(prices):
            max_profit = max(max_profit, prices[i] - buy_prices[i])
            i += 1

        print(max_profit)

        return max_profit

