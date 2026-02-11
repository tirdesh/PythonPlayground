class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        i,j = len(num1)-1, len(num2)-1
        while i>=0 or j>=0 or carry:
            n1 = ord(num1[i]) - ord('0') if i>=0 else 0
            n2 = ord(num2[j]) - ord('0') if j>=0 else 0
            s = n1+n2+carry
            carry = s//10
            s = s%10
            res.append(str(s))
            i-=1
            j-=1
        return "".join(res[::-1])