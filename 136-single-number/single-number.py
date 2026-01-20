class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        seen = set()
        sm = 0
        for i in nums:
            if i not in seen:
                seen.add(i)
                sm+=i
            else:
                sm-=i
        return sm
        """
        res = 0
        for i in nums:
            res^=i
        return res