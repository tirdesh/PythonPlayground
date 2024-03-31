class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Time complexity: O(log n) - The binary search algorithm is employed to find the minimum element. In each iteration of the while loop, the search space is halved, leading to a logarithmic time complexity.
        # Space complexity: O(1) - The algorithm uses a constant amount of extra space regardless of the size of the input list `nums`. It does not utilize any additional data structures that scale with the input size.

        res = nums[0]
        l, r = 0, len(nums) -1
        while l<r:
            if nums[l]< nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r) //2
            res = min(res, nums[m])
            if nums[m] >= nums[r]:
                l = m+1
            else:
                r= m-1
        return res
