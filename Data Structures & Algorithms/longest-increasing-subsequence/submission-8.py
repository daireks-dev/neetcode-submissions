class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def search(i, prev, length):
            if (i, prev) in memo:
                return memo[(i, prev)]
            if i >= len(nums):
                return 0
            
            if nums[i] <= prev:
                res1 = search(i + 1, prev, length)
            else:
                res1 = search(i + 1, nums[i], length + 1) + 1
            res2 = search(i + 1, prev, length)
            memo[(i, prev)] = max(res1, res2)

            return memo[(i, prev)]
        
        return search(0, -1001, 0)

            