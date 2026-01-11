from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_dict = {}
        t_dict = {}
        i = 0
        while i<len(s):
            if s[i] not in s_dict:
                s_dict[s[i]] = 0
            else:
                s_dict[s[i]] += 1
            if t[i] not in t_dict:
                t_dict[t[i]] = 0
            else:
                t_dict[t[i]] += 1
            i+=1
        return s_dict==t_dict