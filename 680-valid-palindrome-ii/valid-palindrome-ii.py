class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        l,r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return is_pal(l,r-1) or is_pal(l+1,r)
            else:
                l+=1
                r-=1
        return True

                