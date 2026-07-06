class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        maxProfit = 0

        while R < len(prices):
            if prices[L] < prices[R]:
                maxProfit = max(maxProfit, prices[R]-prices[L])
            else:
                L = R
            R += 1
        return maxProfit
