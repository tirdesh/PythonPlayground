class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        res = []
        for word in words:
            lword = word.lower()
            if set(lword)<=row1 or set(lword)<=row2 or set(lword)<=row3:
                res.append(word)
        return res