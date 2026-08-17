class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        pos = 31
        while n != 0:
            if n & 1 == 1:
                res += pow(2, pos)
            n >>= 1
            pos -= 1
        
        return res
                