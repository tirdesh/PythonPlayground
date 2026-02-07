import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums)<3:
            return max(nums)
        count = 0
        minheap = []
        for i in nums:
            heapq.heappush(minheap, i)
            count+=1
            if count>3:
                heapq.heappop(minheap)
        return heapq.heappop(minheap)