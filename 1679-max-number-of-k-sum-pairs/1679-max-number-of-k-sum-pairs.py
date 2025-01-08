class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        max_attempt = 0
        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum == k:
                max_attempt += 1
                l += 1
                r -= 1
            elif cur_sum < k:
                l += 1
            else:
                r -= 1
        return max_attempt