class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        
        def search(L, R):
            nonlocal total

            while L >= 0 and R < len(s) and s[L] == s[R]:
                total += 1
                L -= 1
                R += 1
        
        for i in range(len(s)):
            search(i, i)
            search(i, i+1)

        return total
            
            

