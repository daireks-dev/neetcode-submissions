import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if not self.small:
            heapq.heappush(self.small, -num)
        elif len(self.small) > len(self.large):
            if num >= -self.small[0]:
                heapq.heappush(self.large, num)
            else:
                temp = -heapq.heappop(self.small)
                heapq.heappush(self.small, -num)
                heapq.heappush(self.large, temp)
        elif len(self.large) > len(self.small):
            if num <= self.large[0]:
                heapq.heappush(self.small, -num)
            else:
                temp = heapq.heappop(self.large)
                heapq.heappush(self.large, num)
                heapq.heappush(self.small, -temp)
        else:
            if num >= -self.small[0]:
                heapq.heappush(self.large, num)
            else:
                heapq.heappush(self.small, -num)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        return (self.large[0] + -self.small[0]) / 2
        
        