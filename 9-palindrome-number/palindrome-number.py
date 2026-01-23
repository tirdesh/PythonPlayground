class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = x
        if x<0:
            return False
        res=0
        while x!=0:
            res = res*10+(x%10)
            x=x//10
        return s==res
        