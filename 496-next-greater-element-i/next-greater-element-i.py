class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                smaller_num = stack.pop()
                mp[smaller_num] = num
            stack.append(num)
        return [mp.get(num, -1) for num in nums1]