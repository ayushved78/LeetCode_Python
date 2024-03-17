class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin_index = 0
        end_index = len(nums) - 1
        
        while begin_index <= end_index:
#           midpoint is begin point + rest of the values over 2
            midpoint = begin_index + (end_index - begin_index) // 2
            value = nums[midpoint]
            
            if target == value:
                return midpoint
            elif target < value:
                end_index = end_index - 1
            else:
                begin_index = begin_index + 1
            
        return -1