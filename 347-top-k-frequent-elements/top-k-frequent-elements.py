from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i in nums:
            mp[i]+=1
        freq = [[] for i in range(len(nums)+1)]
        for i,v in mp.items():
            freq[v].append(i)
        res = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

            