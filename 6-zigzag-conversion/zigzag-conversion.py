class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res=[[] for _ in range(numRows)]
        j=0
        while j<len(s):
            for i in range(numRows):
                if j<len(s):
                    res[i].append(s[j])
                else:
                    break
                j+=1
            for i in range(numRows-2,0,-1):
                if j<len(s):
                    res[i].append(s[j])
                else:
                    break
                j+=1
        return "".join(["".join(row) for row in res])