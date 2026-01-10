class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
         1111
         1111
        11110 
        """
        s = ""
        i,j = len(a)-1, len(b)-1
        carry = 0
        while i>=0 or j>=0 or carry:
            p = 0 if i<0 else a[i]
            q = 0 if j<0 else b[j]
            tot = int(p)+int(q)+carry
            s=s+str(tot%2)
            carry = tot//2
            i-=1
            j-=1
        return s[::-1]