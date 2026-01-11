class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}
        for i in magazine:
            counts[i] = counts.get(i,0) + 1
        for i in ransomNote:
            if counts.get(i,0)<=0:
                return False
            counts[i]=counts[i]-1
        return True