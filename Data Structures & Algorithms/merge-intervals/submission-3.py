class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals)):
            if i < len(intervals)-1 and intervals[i][1] >= intervals[i+1][0]:
                left = min(intervals[i][0], intervals[i+1][0])
                right = max(intervals[i][1], intervals[i+1][1])
                intervals[i+1] = [left, right]
            else:
                res.append(intervals[i])
        
        return res
