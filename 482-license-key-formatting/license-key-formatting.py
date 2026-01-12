class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        count = 0
        n= len(s)
        res = []
        for i in range(n-1,-1,-1):
            if s[i] == "-":
                continue
            if count==k:
                res.append("-")
                count=0
            res.append(s[i].upper())
            count+=1    
                
        return "".join(res[::-1])