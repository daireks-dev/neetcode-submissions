class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0

        def isPalindrome(s):
            L, R = 0, 1
            while L <= R:
                if s[L] != s[R]:
                    return False
            return True
        
        def search(L, R):
            nonlocal total

            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    total += 1
                else:
                    break

                L -= 1
                R += 1
        
        for i in range(len(s)):
            search(i, i)
            search(i, i+1)

        return total
            
            

