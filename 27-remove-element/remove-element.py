class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k] = nums[i]
                k+=1
        return k
        """
        l=0
        r=len(nums)-1
        while l<=r:
            while r >= 0 and nums[r]==val:
                r-=1
            if l > r:
                break
            if nums[l]==val:
                nums[l],nums[r]=nums[r],nums[l]
            l+=1
        return r+1