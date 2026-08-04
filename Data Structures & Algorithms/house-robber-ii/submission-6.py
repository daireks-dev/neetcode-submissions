class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = {}
        def search(i, end):
            if i in memo:
                return memo[i]
            if i > end:
                return 0
            
            close = nums[i] + search(i+2, end)
            far = search(i+1, end)

            memo[i] = max(close, far)
            return memo[i]
        
        res1 = search(0, len(nums) - 2)

        memo = {}
        res2 = search(1, len(nums) - 1)

        return max(res1, res2)
        
            
