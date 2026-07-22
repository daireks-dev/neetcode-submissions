class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def search(start, subset, subsetSum):
            if subsetSum > target:
                return
            if subsetSum == target:
                res.append(subset)
                return
            
            for i in range(start, len(nums)):
                search(i, subset + [nums[i]], subsetSum + nums[i])
            
        
        search(0, [], 0)
        return res