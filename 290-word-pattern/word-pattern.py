class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        pattern_dict = {}
        used = set()
        if len(s) != len(pattern):
            return False
        
        for i in range(len(s)):
            if s[i] not in pattern_dict:
                if pattern[i] not in used:
                    pattern_dict[s[i]] = pattern[i]
                    used.add(pattern[i])
                else:
                    return False
            elif pattern_dict[s[i]] != pattern[i]:
                return False
        return True

        