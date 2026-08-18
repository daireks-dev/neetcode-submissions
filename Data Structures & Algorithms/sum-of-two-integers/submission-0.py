class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        a &= MASK
        b &= MASK

        while b != 0:
            add = a ^ b
            carry = (a & b) << 1
            a = add & MASK
            b = carry & MASK
        
        if a <= MAX_INT:
            return a
        
        return ~(a ^ MASK)

