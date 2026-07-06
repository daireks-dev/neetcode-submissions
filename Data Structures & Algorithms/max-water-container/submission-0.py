class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i, j = 0, len(heights) - 1

        while i < j:
            res = max(res, (j - i) * min(heights[i], heights[j]))

            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        
        return res
            
            
            