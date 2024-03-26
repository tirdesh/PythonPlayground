class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        # Time complexity: O(n * m * log m) - Constructing sorted strings for each input string, where n is the number of strings in the input list `strs`, and m is the maximum length of the strings in `strs`. Sorting each string takes O(m * log m) time.
        # Space complexity: O(n * m) - Storing sorted strings in `sorted_strs`, and hashmap `d` may hold up to O(n) keys (sorted strings), each with a list of indices, which may have a total of O(n * m) elements.
        sorted_strs = ["".join(sorted(i)) for i in strs]
        print(sorted_strs)
        d = {}
        for i,v in enumerate(sorted_strs):
            if v not in d:
                d[v] = [i]
            else:
                d[v].append(i)
            print(i,v,d)
        res = []
        for i in d:
            res.append([strs[index] for index in d[i]])
        return res
        """
        # Time complexity: O(n * m) - Constructing count arrays for each input string, where n is the number of strings in the input list `strs`, and m is the maximum length of the strings in `strs`.
    # Space complexity: O(n * m) - Storing count arrays in the `map` defaultdict, where each count array is of length 26 (constant space). `map` may hold up to O(n) keys, each with a list of strings, which may have a total of O(n * m) elements.
        map = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord('a')] += 1
            map[tuple(count)].append(i)
        return map.values()
