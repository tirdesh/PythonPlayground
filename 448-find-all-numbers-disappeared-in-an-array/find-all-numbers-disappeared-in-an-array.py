class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums):
            correct_idx = nums[i] - 1
            if nums[i] != nums[correct_idx]:
                nums[correct_idx],nums[i] = nums[i], nums[correct_idx]
            else:
                i+=1
        res = []
        for i,v in enumerate(nums):
            if i+1 != v:
                res.append(i+1)
        return res
