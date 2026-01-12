class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        i = 0
        n = len(s)
        
        while i < n:
            while i < n and s[i] == " ":
                i += 1
            
            if i < n:
                count += 1
                
                while i < n and s[i] != " ":
                    i += 1
                    
        return count