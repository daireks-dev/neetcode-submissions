import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        prefix = suffix = 0

        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1) 
            suffix = nums[n-1-i] * (suffix or 1)
            res = max(res, max(suffix, prefix))
                
        return res
        


        

