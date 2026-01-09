from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        mapChars = {")":"(","}":"{","]":"["}
        arr = []
        for i in s:
            if i not in mapChars:
                arr.append(i)
            if i in mapChars:
                if len(arr)==0:
                    return False
                val = arr.pop()
                if val!=mapChars[i]:
                    return False
        return True if arr==[] else False
            