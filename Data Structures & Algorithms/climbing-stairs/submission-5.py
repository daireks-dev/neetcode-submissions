class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(n):
            if n in memo:
                return memo[n]
            if n <= 2:
                return n
            
            memo[n-1] = climb(n-1)
            memo[n-2] = climb(n-2)

            return memo[n-1] + memo[n-2]
        
        return climb(n)