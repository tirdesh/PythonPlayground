class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        def get_gcd(a,b):
            if b==0:
                return a
            return get_gcd(b,a%b)
        result_len = get_gcd(len(str1), len(str2))
        return str1[:result_len]