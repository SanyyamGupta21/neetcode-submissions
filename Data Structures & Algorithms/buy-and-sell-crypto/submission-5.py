class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxP = 0

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
            else:
                maxP = max(maxP, (prices[sell]-prices[buy]))
                sell += 1
        return maxP