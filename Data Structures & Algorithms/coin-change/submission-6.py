class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        sys.setrecursionlimit(max(1000, amount + 10))

        def search(amountLeft):
            if amountLeft in memo:
                return memo[amountLeft]
            if amountLeft == 0:
                return 0
            
            coinAmount = float("inf")
            for coin in coins:
                if amountLeft >= coin:
                    found = search(amountLeft - coin)
                    if found != float("inf"):
                        coinAmount = min(coinAmount, found + 1)

            memo[amountLeft] = coinAmount
            return memo[amountLeft]
            
        res = search(amount)
        if res == float("inf"):
            return -1
        else:
            return res

