class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result: int = 0

        for i in range(1, len(nums) + 1):
            for c in combinations(nums, i):
                temp: int = 0
                for num in c:
                    temp ^= num
                result += temp

        return result