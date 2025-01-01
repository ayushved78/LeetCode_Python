class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = candies[0]
        res = []
        for i in range(0, len(candies)):
            if candies[i] >= max_val:
                max_val = candies[i]

        for i in range(0,len(candies)):
            if (candies[i]+extraCandies) >= max_val:
                res.append(True)
            else:
                res.append(False)
        return res