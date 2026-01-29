class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        char_count = {}
        res = 0
        max_f = 0
        for r in range(len(s)):
            char_count[s[r]] = char_count.get(s[r],0)+1
            max_f = max(char_count[s[r]],max_f)
            while (r-l+1) - max_f > k:
                char_count[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res
