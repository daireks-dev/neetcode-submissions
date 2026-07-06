class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1 for i in range(n + 1)]
        def dp(n):
            if n <= 2:
                return n
            if cache[n] != -1:
                return cache[n]
            cache[n] = dp(n - 2) + dp(n - 1)
            return cache[n]
        return dp(n)

            
