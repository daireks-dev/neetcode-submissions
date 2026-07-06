class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        index = 0
        for num in nums:
            difference = target - num
            if difference in seen:
                return [seen[difference], index]

            seen[num] = index
            index += 1