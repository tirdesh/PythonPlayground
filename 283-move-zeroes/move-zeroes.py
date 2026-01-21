class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        i,j = 0,0
        while i<len(nums):
            while i<len(nums) and nums[i]!=0:
                i+=1
            j=i+1
            while j<len(nums) and nums[j]==0:
                j+=1
            if i<len(nums) and j<len(nums):
                nums[i],nums[j] = nums[j], nums[i]
            i+=1
        """
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index+=1
        