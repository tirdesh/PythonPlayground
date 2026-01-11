from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counts = {}
        for i in s:
            counts[i] = counts.get(i,0) + 1
        for j in t:
            counts[j] = counts.get(j,0) - 1
        return all(v==0 for v in counts.values())
        """
        if len(s)!=len(t):
            return False
        s_dict = {}
        t_dict = {}
        i = 0
        while i<len(s):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1
            i+=1
        return s_dict==t_dict
        """