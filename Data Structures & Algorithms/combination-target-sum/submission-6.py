class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def search(start, subset, subsetSum):
            if subsetSum == target:
                res.append(subset.copy())
                return
            
            for i in range(start, len(nums)):
                if subsetSum + nums[i] > target:
                    return
                subset.append(nums[i])
                search(i, subset, subsetSum + nums[i])
                subset.pop()
            
        
        search(0, [], 0)
        return res