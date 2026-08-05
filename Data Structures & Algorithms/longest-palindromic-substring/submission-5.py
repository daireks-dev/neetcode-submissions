class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        longest = (0,0)
        def search(L, R):
            nonlocal longest

            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    if longest[1] - longest[0] < R-L:
                        longest = (L, R)
                else:
                    break
                
                L -= 1
                R += 1

        for i in range(0, len(s)):
            search(i, i)
            search(i, i + 1)

        return s[longest[0]:longest[1]+1]



