class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = min_candies = candies[0]
        for i in candies:
            max_candies = i if i>max_candies else max_candies
        res = []
        for i in candies:
            res.append(True if i+extraCandies>=max_candies else False)
        return res