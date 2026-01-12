class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        # Mask to handle 32-bit two's complement for negative numbers
        num &= 0xFFFFFFFF
        hexmap = "0123456789abcdef"
        res = ""
        while num>0:
            rem = num%16
            res = hexmap[rem]+res
            num = num//16
        return res