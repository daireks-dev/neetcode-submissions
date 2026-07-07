class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        L = 0
        greatestFrequency = 0
        count = {}

        for R in range(0, len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            greatestFrequency = max(greatestFrequency, count[s[R]])

            while ((R - L) + 1 - greatestFrequency > k):
                count[s[L]] -= 1
                L += 1

            res = max(res, (R - L) + 1)
        
        return res

