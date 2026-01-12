class Solution:
    def longestPalindrome(self, s: str) -> int:
        ct = {}
        for i in s:
            ct[i] = ct.get(i,0)+1
        summ=0
        flag=0
        
        for i in ct.values():
            if i%2!=0:
                flag = 1
                summ=summ+((i//2)* 2)
            else:
                summ=summ+i
        print(ct,summ)
        return summ+1 if flag else summ

