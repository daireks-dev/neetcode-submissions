class Solution:
    def minWindow(self, s: str, t: str) -> str:
        windowCount, stringCount = {}, {}
        for char in t:
            stringCount[char] = stringCount.get(char, 0) + 1

        have, need = 0, len(stringCount)
        foundSubstring, foundLength = [-1, -1], float("infinity")

        L = 0
        for R in range(0, len(s)):
            char = s[R]
            windowCount[char] = windowCount.get(char, 0) + 1

            if char in stringCount and windowCount[char] == stringCount[char]:
                have += 1
            
            while have == need:
                if (R - L + 1) < foundLength:
                    foundSubstring = [L, R]
                    foundLength = R - L + 1
                windowCount[s[L]] -= 1
                if s[L] in stringCount and windowCount[s[L]] < stringCount[s[L]]:
                    have -= 1
                L += 1

        L, R = foundSubstring
        return s[L: R + 1] if foundLength != float("infinity") else ""

