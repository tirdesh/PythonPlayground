class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Time complexity: O(n) - The code iterates through the list `height` once using two pointers (`i` and `j`), where `n` is the length of the list. Each iteration involves constant-time operations, such as computing the area and updating the maximum area. Therefore, the overall time complexity is linear with respect to the length of the input list.
        # Space complexity: O(1) - The code uses only a constant amount of extra space regardless of the size of the input list. It does not utilize any additional data structures that scale with the input size.
        res = 0
        i,j = 0,len(height) - 1
        while i<j:
            area = min(height[i],height[j]) * (j-i)
            res = max(area, res)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return res
