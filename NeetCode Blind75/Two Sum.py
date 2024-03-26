class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        # Time complexity: O(n^2) - nested loops
        # Space complexity: O(1) - constant space
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
        """
        # Time complexity: O(n) - linear time, loop through nums once
        # Space complexity: O(n) - num_indices dictionary
        x={}
        for i,v in enumerate(nums):
            res = target-v
            if res in x:
                return [i, x[res]]
            x[nums[i]] = i
        """
        # Time complexity: O(n log n) - sort(n log n) & loop (n)
        # Space complexity: O(n) - num_indices(n)
        num_indices = {}  
        for idx, num in enumerate(nums):
            if num not in num_indices:
                num_indices[num] = [idx]
            else:
                num_indices[num].append(idx)
        sNums = sorted(nums)
        i=0
        j=len(sNums) - 1
        while i!=j:
            if sNums[i]+sNums[j] == target:
                return [num_indices[sNums[i]][0], num_indices[sNums[j]][-1]]
            elif sNums[i]+sNums[j] > target:
                j-=1
            elif sNums[i]+sNums[j] < target:
                i+=1
        """
