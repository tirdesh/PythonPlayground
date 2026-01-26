class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        res = []
        n = len(nums)
        for i in range(n):
            res.append(mul)
            mul = mul*nums[i]
        mul = 1
        for i in range(n-1,-1,-1):
            res[i] *= mul
            mul = mul*nums[i]
        return res