class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        min_first = max(0, n - 2 * limit)
        max_first = min(n, limit)
        ways = 0
        for i in range(min_first, max_first + 1):
            N = n - i
            min_ch2 = max(0, N - limit)
            max_ch2 = min(N, limit)
            ways += max_ch2 - min_ch2 + 1
        return ways