class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if needle == haystack[i:i+k]:
                    return i
        return -1