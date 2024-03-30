class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time complexity: O(n) - Iterates through the characters of the string `s` once using two pointers (`l` and `r`), processing each character only once in the while loop.
        # Space complexity: O(min(n, k)) - Uses a set `a` to store unique characters encountered in the current substring. The space complexity is bounded by the size of the character set (usually 256 for ASCII characters) or the length of the string, whichever is smaller.
        a = set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in a:
                a.remove(s[l])
                l+=1
            a.add(s[r])
            res = max(res, r-l+1)
        return res
