class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def search(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1

            if s[i] != "0":
                res1 = search(i + 1)
            else:
                return 0

            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                res2 = search(i + 2)
            else:
                res2 = 0
            
            
            memo[i] = res1 + res2

            return memo[i]
            

        return search(0)
            
