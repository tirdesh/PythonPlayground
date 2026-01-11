class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapIso = {}
        used = set()
        i=0
        while i<len(s):
            if s[i] not in mapIso:
                if t[i] in used:
                    return False
                mapIso[s[i]] = t[i]
                used.add(t[i])
            elif mapIso[s[i]] != t[i]:
                return False
            i+=1
        return True

        