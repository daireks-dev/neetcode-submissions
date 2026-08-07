class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def search(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            ways = search(i + 1)

            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                ways += search(i + 2)        
            
            memo[i] = ways

            return memo[i]
            

        return search(0)
            
