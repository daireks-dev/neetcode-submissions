class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def search(start, subset, subsetSum):
            if subsetSum > target:
                return
            if subsetSum == target:
                res.append(subset.copy())
                return
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                search(i, subset, subsetSum + nums[i])
                subset.pop()
            
        
        search(0, [], 0)
        return res