class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map = {v:i for i,v in enumerate(list1)}
        min_sum = float('inf')
        ans = []

        for i,v in enumerate(list2):
            if v in map:
                current_sum = map[v]+i
                if current_sum < min_sum:
                    min_sum = current_sum
                    ans = [v]
                elif current_sum == min_sum:
                    ans.append(v)
        return ans



            
        