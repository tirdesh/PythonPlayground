class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=-1
        for k in range(n-2,-1,-1):
            if nums[k]<nums[k+1]:
                i=k
                break
        if i>=0:
            for j in range(n-1,-1,-1):
                if nums[j]>nums[i]:
                    nums[i],nums[j] = nums[j],nums[i]
                    break
        l=i+1
        r=n-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        

            
        
        
        
