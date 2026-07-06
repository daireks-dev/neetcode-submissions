class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res


    def decode(self, s: str) -> List[str]:
        found = []
        i = 0
        j = 0
        while i < len(s):
            if s[j] != "#":
                j += 1
            else:
                length = int(s[i:j])
                found.append(s[j+1:j+length+1])
                i = j+length+1
                j = i

        return found
                
            


