class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i,v in enumerate(nums):
            rem = target - v
            if rem in mp:
                return [i,mp[rem]]
            mp[v] = i
        