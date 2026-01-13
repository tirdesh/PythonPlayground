class Solution:
    def checkRecord(self, s: str) -> bool:
        #return s.count('A')<2 and 'LLL' not in s
        acount = 0
        i=0
        while i<len(s):
            if s[i] == "A":
                acount+=1
                if acount>=2:
                    return False
                i+=1
            elif s[i] == "L":
                lcount=0
                while i<len(s) and s[i] == "L":
                    lcount+=1
                    i+=1
                    if lcount==3:
                        return False
            else:
                i+=1
        return True
