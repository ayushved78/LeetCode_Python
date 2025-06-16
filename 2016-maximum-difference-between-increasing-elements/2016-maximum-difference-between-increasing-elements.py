class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_so_far = nums[0]
        max_diff = -1

        for j in range(1, len(nums)):
            if nums[j] > min_so_far:
                max_diff = max(max_diff, nums[j] - min_so_far)
            else:
                min_so_far = nums[j]

        return max_diff
