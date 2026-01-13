class Solution:
    def reverseWords(self, s: str) -> str:
        sl = list(s)
        i = 0
        while i<len(sl):
            l=i
            while i<len(sl) and sl[i] != " ":
                i+=1
            r=i-1
            i+=1
            while l<=r:
                sl[l],sl[r] = sl[r],sl[l]
                l+=1
                r-=1
        return "".join(sl)
            
        