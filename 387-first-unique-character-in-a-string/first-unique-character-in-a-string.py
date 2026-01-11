class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = -1
        used = set()
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1
        for i in count:
            if count[i] == 1:
                return s.find(i)
        return ans

            