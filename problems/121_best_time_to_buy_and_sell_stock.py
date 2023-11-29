class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price, max_price = prices[0], prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
                max_price = price
                continue
            if price > max_price:
                max_price = price
                max_profit = max(max_profit, max_price - min_price)

        return max_profit
