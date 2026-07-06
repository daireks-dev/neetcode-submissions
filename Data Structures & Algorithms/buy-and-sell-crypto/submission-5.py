class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L, R = 0, 1

        while R < len(prices):
            res = max(res, prices[R] - prices[L])
            if prices[R] >= prices[L]:
                R += 1
            else:
                L = R
                R += 1
        
        return res

