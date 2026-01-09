class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        l_str = strs[0]
        for i in strs:
            if len(l_str)>len(i):
                l_str = i
        for i in l_str:
            mc = 0
            for j in strs:
                if j.startswith(res + i):
                    mc += 1
            if mc == len(strs):
                res = res+i
        return res