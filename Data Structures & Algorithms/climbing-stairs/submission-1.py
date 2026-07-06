class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dp(n):
            if n <= 2:
                return n
            cache[n] = dp(n - 2) + dp(n - 1)
            return cache[n]
        return dp(n)

            
