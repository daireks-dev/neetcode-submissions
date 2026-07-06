class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L, R = 0, 1

        while R < len(prices):
            if prices[R] >= prices[L]:
                res = max(res, prices[R] - prices[L])
            else:
                L = R
            R += 1
        return res

