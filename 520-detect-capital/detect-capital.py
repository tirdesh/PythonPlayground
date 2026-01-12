class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        n = len(word)
        for i in word:
            if ord("A")<=ord(i)<=ord("Z"):
                count+=1
        print(count)
        if count == 0:
            return True
        if count == n:
            return True
        if count == 1 and ord("A")<=ord(word[0])<=ord("Z"):
            return True
        return False