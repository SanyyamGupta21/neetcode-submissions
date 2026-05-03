import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = prices[0]

        for i in prices:
            maxP = max(maxP, i - buy)
            buy = min(buy, i)   
        return maxP