class Solution:
    def addDigits(self, num: int) -> int:
        n=0
        while num:
            n+=num%10
            num//=10
            if num==0 and n%10!=n:
                num=n
                n=0
        return n