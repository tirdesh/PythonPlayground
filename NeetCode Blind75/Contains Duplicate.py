class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time complexity: O(n) - Looping through the list once
        # Space complexity: O(n) - Using a set to store unique elements
        s= set()
        for i in sorted(nums):
            if i in s:
                return True
            s.add(i)
        return False
