class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x_List = list(str(abs(x)))
        l = 0
        r = len(x_List)-1
        while l<r:
            x_List[l],x_List[r] = x_List[r],x_List[l]
            l+=1
            r-=1
        ans = abs(int("".join(x_List)))
        if ans>2**31:
            return 0
        else:
            return sign*ans
            