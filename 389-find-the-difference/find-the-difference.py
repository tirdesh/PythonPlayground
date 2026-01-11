class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        seen = [] 
        for i in s:
            seen.append(i)
        for i in t:
            if i not in seen:
                return i
            else:
                seen.remove(i)
        return seen[0]
        """
        """
        count = {}
        for i in s:
            count[i] = count.get(i,0)+1
        for i in t:
            if i not in count or count[i] == 0:
                return i
            count[i]-=1
        """
        return chr(sum(ord(c) for c in t) - sum(ord(c) for c in s))