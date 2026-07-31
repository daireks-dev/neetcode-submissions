class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = {}
        def search(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return
            if i >= len(nums) - 2:
                return nums[i]
            
            close = nums[i] + search(i+2)
            far = search(i + 1)
            memo[i] = max(close, far)

            return memo[i]
        
        return max(search(0), search(1))
