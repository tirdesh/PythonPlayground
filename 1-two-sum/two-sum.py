class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,v in enumerate(nums):
            k = target-v
            if k in d:
                return [i,d[k]]
            d[v] = i