class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        cur_num = nums[0]
        longest = 1
        l = 0
        
        for r in range(1, len(nums)):
            while l != r and nums[r] & cur_num != 0:
                cur_num -= nums[l]
                l += 1
            
            longest = max(longest, r - l + 1)
            cur_num += nums[r]
        
        
        return longest