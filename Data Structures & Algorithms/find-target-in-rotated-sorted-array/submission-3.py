class Solution:
    def search(self, nums: List[int], target: int) -> int:
        edgeIndex = 0
        L, R = 0, len(nums) - 1

        while L <= R:
            if nums[L] <= nums[R]:
                if nums[L] < nums[edgeIndex]:
                    edgeIndex = L
                break
            
            mid = (L + R) // 2
            if nums[mid] < nums[edgeIndex]:
                    edgeIndex = mid

            if nums[L] <= nums[mid]:
                L = mid + 1
            else:
                R = mid - 1
        
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            realMid = (mid + edgeIndex) % len(nums)
            if nums[realMid] > target:
                R = mid - 1
            elif nums[realMid] < target:
                L = mid + 1
            else:
                return realMid
        
        return -1
