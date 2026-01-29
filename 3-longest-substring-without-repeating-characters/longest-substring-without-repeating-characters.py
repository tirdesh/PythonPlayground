class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        l=0
        seen = set()
        maxlen = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[i])
            maxlen = max(i-l+1,maxlen)
        return maxlen
        """
        l=maxlen=0
        char_map = {}
        for r in range(len(s)):
            if s[r] in char_map:
                l= max(l,char_map[s[r]]+1)
            char_map[s[r]]=r
            maxlen = max(r-l+1,maxlen)
        return maxlen
