class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        freq_map = [0]*(len(nums)+max(nums)+1)
        for v in nums:
            freq_map[v] += 1
        res = 0
        for key in range(len(freq_map)):
            if freq_map[key]>1:
                dup = freq_map[key]-1
                freq_map[key] -= dup
                freq_map[key+1] += dup
                res+=dup
        print([i for i,v in enumerate(freq_map) if v == 1])
        return res