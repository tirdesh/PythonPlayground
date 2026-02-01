import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = [] # -ve and store, so it acts like maxheap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap)-len(self.max_heap)>1:
            pop = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -pop)

    def findMedian(self) -> float:
        if len(self.min_heap)>len(self.max_heap):
            return self.min_heap[0]
        else:
            return (self.min_heap[0]+(-1)*(self.max_heap[0]))/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()