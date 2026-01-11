class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen = [] 
        for i in s:
            seen.append(i)
        for i in t:
            if i not in seen:
                return i
            else:
                seen.remove(i)
        return seen[0]
        