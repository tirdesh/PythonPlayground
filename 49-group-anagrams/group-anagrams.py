class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp  = {}
        for i in strs:
            c_list = [0]*26
            for j in i:
                c_list[ord(j)-ord('a')] += 1
            c_tup = tuple(c_list)
            if c_tup not in mp:
                mp[c_tup] = [i]
            else:
                mp[c_tup].append(i)
        return [mp[i] for i in mp]
