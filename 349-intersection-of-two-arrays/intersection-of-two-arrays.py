class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = set()
        res = set()
        for v in nums1:
            mp.add(v)
        for v in nums2:
            if v in mp:
                res.add(v)
        return list(res)