class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        maxLength = 0
        L, R = 0, 1
        seen = set()
        seen.add(s[L])
        while R < len(s):
            print(L, R)
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            maxLength = max(R - L + 1, maxLength)
            R += 1
        return maxLength

