class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        a &= MASK
        b &= MASK

        while b != 0:
            temp = (a & b) << 1
            a = (a ^ b) & MASK
            b = (temp) & MASK
        
        if a <= MAX_INT:
            return a
        
        return ~(a ^ MASK)

