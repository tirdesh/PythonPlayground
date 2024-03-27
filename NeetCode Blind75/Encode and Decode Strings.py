class Solution:
    
    def encode(self, strs: List[str]) -> str:
        # Time complexity for encode: O(n), where n is the total number of characters in all strings in the input list `strs`. This is because the function iterates through each string in `strs` once, and concatenating each string takes linear time.
        # Space complexity for encode: O(n), where n is the total number of characters in all strings in the input list `strs`. This is because the function creates a new string `encodedStr` to store the concatenated strings, and its size grows linearly with the total number of characters in `strs`.
        encodedStr = ""
        for i in strs:
            encodedStr = encodedStr + i + "#@#"
        return encodedStr

    def decode(self, s: str) -> List[str]:
        # Time complexity for decode: O(n), where n is the length of the input string `s`. This is because the function splits the input string `s` using the delimiter "#@#" to separate the encoded strings, which takes linear time.
        # Space complexity for decode: O(n), where n is the length of the input string `s`. This is because the function splits the input string `s` into substrings, resulting in a list of substrings, each taking up space proportional to its length.
        return s.split("#@#")[:-1]
