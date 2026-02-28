class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        freq = [0] * 26
        for i in letters:
            freq[ord(i)-ord('a')]+=1
        target_num = ord(target) - ord('a')
        for i in range(target_num+1,26):
            if freq[i]!=0:
                return chr(i+ord('a'))
        return letters[0]
