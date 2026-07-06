class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = {}
        L, R = 0, 0

        while R < len(s):
            if not s[R] in seen:
                seen[s[R]] = 1
                R += 1
                res = max(res, R - L)
            else:
                seen.pop(s[L])
                L += 1
            
        return res
            
            
