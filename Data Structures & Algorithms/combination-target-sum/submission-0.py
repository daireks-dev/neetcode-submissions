class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def search(nums, subset, subsetSum):
            if subsetSum > target:
                return
            if subsetSum == target:
                res.append(subset)
                return
            
            for i, n in enumerate(nums):
                search(nums[i:], subset + [n], subsetSum + n)
            
        
        search(nums, [], 0)
        return res