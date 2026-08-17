class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def search(i, prev):
            if (i, prev) in memo:
                return memo[(i, prev)]
            if i >= len(nums):
                return 0
            
            if nums[i] > prev:
                res1 = search(i + 1, nums[i]) + 1
                res2 = search(i + 1, prev)
                memo[(i, prev)] = max(res1, res2)
            else:
                memo[(i, prev)] = search(i + 1, prev)

            return memo[(i, prev)]
        
        return search(0, -1001)

            