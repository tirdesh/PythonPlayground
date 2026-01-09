class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        for i in s[::-1]:
            if i != " ":
                l+=1
            elif l==0:
                continue
            else:
                break
        return l
        