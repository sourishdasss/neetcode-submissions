class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_price = []

        cheapest_price.append(prices[0])

        for i in range(1, len(prices)):
            cheapest_price.append(min(cheapest_price[i-1], prices[i]))

        highest_diff = 0

        for i in range(len(prices)):
            highest_diff = max(highest_diff, prices[i] - cheapest_price[i])

        return highest_diff

