class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=len(t)
        i,j = 0,0
        while j<n and i<len(s):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
            print(i,j)
        return i==len(s)