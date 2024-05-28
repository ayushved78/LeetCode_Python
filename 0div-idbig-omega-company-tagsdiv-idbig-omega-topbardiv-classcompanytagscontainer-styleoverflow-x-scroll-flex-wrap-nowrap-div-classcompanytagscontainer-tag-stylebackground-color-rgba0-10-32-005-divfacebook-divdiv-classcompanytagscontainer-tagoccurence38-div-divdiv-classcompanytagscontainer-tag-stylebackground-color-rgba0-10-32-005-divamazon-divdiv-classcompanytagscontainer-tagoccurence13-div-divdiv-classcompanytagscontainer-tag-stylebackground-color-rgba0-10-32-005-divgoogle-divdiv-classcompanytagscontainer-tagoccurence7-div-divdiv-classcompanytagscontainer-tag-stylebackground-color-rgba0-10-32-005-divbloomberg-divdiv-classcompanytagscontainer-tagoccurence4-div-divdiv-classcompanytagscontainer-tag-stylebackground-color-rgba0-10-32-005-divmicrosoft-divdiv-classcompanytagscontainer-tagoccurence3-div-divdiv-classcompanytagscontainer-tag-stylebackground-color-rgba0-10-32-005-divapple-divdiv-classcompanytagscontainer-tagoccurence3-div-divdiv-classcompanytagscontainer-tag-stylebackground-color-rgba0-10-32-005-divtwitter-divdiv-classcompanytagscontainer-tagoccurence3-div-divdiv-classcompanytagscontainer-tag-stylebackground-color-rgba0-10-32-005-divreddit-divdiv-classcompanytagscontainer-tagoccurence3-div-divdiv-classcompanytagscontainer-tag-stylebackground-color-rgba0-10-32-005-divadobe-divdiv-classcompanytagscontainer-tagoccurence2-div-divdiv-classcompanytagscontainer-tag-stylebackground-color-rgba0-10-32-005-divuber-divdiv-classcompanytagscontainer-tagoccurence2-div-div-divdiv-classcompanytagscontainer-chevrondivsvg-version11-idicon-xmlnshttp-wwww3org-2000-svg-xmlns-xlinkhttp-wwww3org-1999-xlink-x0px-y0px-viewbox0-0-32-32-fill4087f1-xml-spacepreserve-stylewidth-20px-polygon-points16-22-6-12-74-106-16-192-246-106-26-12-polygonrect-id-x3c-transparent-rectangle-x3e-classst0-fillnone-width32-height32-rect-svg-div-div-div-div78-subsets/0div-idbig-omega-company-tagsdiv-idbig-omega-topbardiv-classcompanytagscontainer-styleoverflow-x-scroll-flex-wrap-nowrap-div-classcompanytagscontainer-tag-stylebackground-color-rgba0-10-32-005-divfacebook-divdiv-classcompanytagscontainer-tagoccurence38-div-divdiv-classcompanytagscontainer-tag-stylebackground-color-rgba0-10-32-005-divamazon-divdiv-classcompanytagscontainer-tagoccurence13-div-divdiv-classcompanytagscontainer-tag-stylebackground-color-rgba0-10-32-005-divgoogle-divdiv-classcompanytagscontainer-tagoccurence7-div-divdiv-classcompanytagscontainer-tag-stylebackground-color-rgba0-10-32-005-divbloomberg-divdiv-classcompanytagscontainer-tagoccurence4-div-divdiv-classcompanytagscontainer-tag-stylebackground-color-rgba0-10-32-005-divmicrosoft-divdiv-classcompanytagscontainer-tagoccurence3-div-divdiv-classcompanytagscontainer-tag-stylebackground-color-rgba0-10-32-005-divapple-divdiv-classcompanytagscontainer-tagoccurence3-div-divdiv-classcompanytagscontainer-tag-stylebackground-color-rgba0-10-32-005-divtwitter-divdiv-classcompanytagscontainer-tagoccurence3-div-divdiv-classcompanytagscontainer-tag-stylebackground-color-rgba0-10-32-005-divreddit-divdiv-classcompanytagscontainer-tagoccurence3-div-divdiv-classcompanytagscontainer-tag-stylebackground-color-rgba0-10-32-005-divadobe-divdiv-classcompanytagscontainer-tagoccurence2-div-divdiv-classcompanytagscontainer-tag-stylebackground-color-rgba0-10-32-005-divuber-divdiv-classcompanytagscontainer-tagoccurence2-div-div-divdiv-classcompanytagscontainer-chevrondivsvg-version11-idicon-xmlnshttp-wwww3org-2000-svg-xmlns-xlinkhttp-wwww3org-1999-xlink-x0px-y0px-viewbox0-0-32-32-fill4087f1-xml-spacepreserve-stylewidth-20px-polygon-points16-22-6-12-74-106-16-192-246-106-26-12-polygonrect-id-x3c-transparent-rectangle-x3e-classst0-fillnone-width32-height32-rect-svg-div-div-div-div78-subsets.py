class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for i in nums:
            output += [lst + [i] for lst in output]
        return output