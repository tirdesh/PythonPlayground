class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        k=len(needle)
        for i in range(len(haystack)-k+1):
            if haystack[i] == needle[0]and needle == haystack[i:i+k]:
                    return i
        return -1