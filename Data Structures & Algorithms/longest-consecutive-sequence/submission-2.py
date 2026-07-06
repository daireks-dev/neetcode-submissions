class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()
        
        currentSequence = [nums[0]]
        longestSequence = currentSequence
        lastNum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == lastNum:
                continue
            if nums[i] == lastNum + 1:
                currentSequence.append(nums[i])
                lastNum = nums[i]
                if len(currentSequence) > len(longestSequence):
                    longestSequence = currentSequence
            else:
                currentSequence = [nums[i]]
                lastNum = nums[i]
        
        return len(longestSequence)
