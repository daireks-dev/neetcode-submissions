class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        primaryChar = None
        primaryCharFrequency = 0

        frequency = {}
        L, R = 0, 0

        while R < len(s):
            if s[R] in frequency:
                frequency[s[R]] += 1
            else:
                frequency[s[R]] = 1

            if frequency[s[R]] > primaryCharFrequency:
                primaryChar = s[R]
                primaryCharFrequency = frequency[s[R]]
            
            replacements = 0
            for char in frequency.keys():
                if char != primaryChar:
                    replacements += frequency[char]

            if replacements > k:
                frequency[s[L]] -= 1
                L += 1
                
            res = max(res, R - L + 1)
            R += 1
        
        return res

