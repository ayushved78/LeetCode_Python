class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # assign 1 candy to each child
        candies = [1] * n

        # go L->to->R
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        # go R->to->L
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i+1]+1)

        return sum(candies)