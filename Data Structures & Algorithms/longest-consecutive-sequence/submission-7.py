class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet:
                i = 1
                while num + i in numSet:
                    i += 1
                longest = max(longest, i)

        return longest

