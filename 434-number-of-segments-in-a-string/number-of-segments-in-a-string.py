class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        i=0
        n=len(s)
        while i<n:
            while i<n and s[i]==" ":
                i+=1
            if i == n: break
            j=i
            while j<n and s[j]!=" ":
                j+=1
            count+=1
            i=j
        return count