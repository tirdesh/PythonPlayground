class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=maxlen=0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxlen= max(r-l+1,maxlen)
        return maxlen
