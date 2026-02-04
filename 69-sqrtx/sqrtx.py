class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        lo,hi = 1,x//2
        ans = lo
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if mid*mid == x:
                return mid
            elif mid*mid<=x:
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
        return ans
                