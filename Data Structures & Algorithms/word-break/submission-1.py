class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def search(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return True

            for word in wordDict:
                if word == s[i:i+len(word)]:
                    memo[i] = search(i + len(word))
                    if memo[i] == True:
                        return True

            return False

        return search(0)
            

