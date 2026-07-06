class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        string = s.lower()
        i, j = 0, len(string)-1

        while i <= j:
            while not string[i].isalnum():
                i += 1
                if i == len(s) - 1:
                    return True
            while not string[j].isalnum():
                j -= 1
                if j == len(s) - 1:
                    return True

            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        
        return True