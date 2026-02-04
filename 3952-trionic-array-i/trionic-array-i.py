class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i=0
        n= len(nums)
        while i<n-3 and nums[i]<nums[i+1]:
            i+=1
        p=i
        if p==0 or p==n-2:
            return False
        while i<n-2 and nums[i]>nums[i+1]:
            i+=1
        q=i
        if q==p or q==n-1:
            return False
        while i<n-1 and nums[i]<nums[i+1]:
            i+=1
        if i!=n-1:
            return False
        else:
            return True