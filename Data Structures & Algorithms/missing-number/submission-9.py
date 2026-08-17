class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            total += n
        
        expected = 0
        for n in range(len(nums) + 1):
            expected += n

        print(total, expected)
        
        return expected - total
        

