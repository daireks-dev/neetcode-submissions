class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        array1 = nums[0:len(nums)-1]
        array2 = nums[1:len(nums)]
        
        memo = {}
        def search(array, i):
            if i in memo:
                return memo[i]
            if i >= len(array):
                return 0
            
            close = array[i] + search(array, i+2)
            far = search(array, i+1)

            memo[i] = max(close, far)
            return memo[i]
        
        res1 = search(array1, 0)

        memo = {}
        res2 = search(array2, 0)

        return max(res1, res2)
        
            
