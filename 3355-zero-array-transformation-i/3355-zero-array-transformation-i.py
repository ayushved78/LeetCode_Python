class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1
        cover = 0
        for i in range(n):
            cover += diff[i]
            if cover < nums[i]:
                return False
        return True