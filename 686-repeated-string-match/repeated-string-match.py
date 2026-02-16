class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = ceil(len(b)/len(a))
        temp = a*count
        if b in temp:
            return count
        elif b in temp+a:
            return count+1
        else:
            return -1