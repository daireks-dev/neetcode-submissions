class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s[0]

        longest = ""
        for i in range(0, len(s)):
            L, R = i, i
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    if len(longest) < len(s[L:R+1]):
                        longest = s[L:R+1]
                else:
                    break
                
                L -= 1
                R += 1

            L, R = i, i + 1
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    if len(longest) < len(s[L:R+1]):
                        longest = s[L:R+1]
                else:
                    break
                
                L -= 1
                R += 1
            
        return longest



