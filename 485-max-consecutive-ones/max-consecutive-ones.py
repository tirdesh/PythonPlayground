class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s=0
        ans = 0
        for i in nums:
            if i==0:
                ans = max(ans,s)
                s=0
            s+=i
        return max(ans,s)
            
