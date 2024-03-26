class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        # Time complexity: O(n log n) - Sorting both strings
        # Space complexity: O(n) - Creating sorted strings
        return sorted(s) == sorted(t)
        """
        # Time complexity: O(n) - Looping through both strings once
        # Space complexity: O(1) - Constant space, using a hashmap
        if len(s) != len(t):
            return False
        d = {}
        for i in s:
            d[i] = d.get(i,0)+1
        for i in t:
            if i not in d:
                return False
            d[i] = d[i]-1
            if d[i]==0:
                del d[i]

        if d=={}:
            return True
