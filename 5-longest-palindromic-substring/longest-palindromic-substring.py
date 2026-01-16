class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        for i in range(len(s)):
            self.expand(s,i,i)
            self.expand(s,i,i+1)
        return self.res
            
    def expand(self, s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            if r-l+1>len(self.res):
                self.res=s[l:r+1]
            l-=1
            r+=1

        