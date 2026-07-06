class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = defaultdict(list)
        topCount = 1

        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > topCount:
                topCount = count[num]

        for num in count:
            freq[count[num]].append(num)
        
        res = []
        while len(res) < k:
            for num in freq[topCount]:
                res.append(num)
            topCount -= 1
            
        return res

        
        
        