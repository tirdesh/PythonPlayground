class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxlen = 0
        for num in seen:
            if num-1 not in seen:
                end = num+1
                while end in seen:
                    end+=1
                maxlen = max(end-num,maxlen)
        return maxlen