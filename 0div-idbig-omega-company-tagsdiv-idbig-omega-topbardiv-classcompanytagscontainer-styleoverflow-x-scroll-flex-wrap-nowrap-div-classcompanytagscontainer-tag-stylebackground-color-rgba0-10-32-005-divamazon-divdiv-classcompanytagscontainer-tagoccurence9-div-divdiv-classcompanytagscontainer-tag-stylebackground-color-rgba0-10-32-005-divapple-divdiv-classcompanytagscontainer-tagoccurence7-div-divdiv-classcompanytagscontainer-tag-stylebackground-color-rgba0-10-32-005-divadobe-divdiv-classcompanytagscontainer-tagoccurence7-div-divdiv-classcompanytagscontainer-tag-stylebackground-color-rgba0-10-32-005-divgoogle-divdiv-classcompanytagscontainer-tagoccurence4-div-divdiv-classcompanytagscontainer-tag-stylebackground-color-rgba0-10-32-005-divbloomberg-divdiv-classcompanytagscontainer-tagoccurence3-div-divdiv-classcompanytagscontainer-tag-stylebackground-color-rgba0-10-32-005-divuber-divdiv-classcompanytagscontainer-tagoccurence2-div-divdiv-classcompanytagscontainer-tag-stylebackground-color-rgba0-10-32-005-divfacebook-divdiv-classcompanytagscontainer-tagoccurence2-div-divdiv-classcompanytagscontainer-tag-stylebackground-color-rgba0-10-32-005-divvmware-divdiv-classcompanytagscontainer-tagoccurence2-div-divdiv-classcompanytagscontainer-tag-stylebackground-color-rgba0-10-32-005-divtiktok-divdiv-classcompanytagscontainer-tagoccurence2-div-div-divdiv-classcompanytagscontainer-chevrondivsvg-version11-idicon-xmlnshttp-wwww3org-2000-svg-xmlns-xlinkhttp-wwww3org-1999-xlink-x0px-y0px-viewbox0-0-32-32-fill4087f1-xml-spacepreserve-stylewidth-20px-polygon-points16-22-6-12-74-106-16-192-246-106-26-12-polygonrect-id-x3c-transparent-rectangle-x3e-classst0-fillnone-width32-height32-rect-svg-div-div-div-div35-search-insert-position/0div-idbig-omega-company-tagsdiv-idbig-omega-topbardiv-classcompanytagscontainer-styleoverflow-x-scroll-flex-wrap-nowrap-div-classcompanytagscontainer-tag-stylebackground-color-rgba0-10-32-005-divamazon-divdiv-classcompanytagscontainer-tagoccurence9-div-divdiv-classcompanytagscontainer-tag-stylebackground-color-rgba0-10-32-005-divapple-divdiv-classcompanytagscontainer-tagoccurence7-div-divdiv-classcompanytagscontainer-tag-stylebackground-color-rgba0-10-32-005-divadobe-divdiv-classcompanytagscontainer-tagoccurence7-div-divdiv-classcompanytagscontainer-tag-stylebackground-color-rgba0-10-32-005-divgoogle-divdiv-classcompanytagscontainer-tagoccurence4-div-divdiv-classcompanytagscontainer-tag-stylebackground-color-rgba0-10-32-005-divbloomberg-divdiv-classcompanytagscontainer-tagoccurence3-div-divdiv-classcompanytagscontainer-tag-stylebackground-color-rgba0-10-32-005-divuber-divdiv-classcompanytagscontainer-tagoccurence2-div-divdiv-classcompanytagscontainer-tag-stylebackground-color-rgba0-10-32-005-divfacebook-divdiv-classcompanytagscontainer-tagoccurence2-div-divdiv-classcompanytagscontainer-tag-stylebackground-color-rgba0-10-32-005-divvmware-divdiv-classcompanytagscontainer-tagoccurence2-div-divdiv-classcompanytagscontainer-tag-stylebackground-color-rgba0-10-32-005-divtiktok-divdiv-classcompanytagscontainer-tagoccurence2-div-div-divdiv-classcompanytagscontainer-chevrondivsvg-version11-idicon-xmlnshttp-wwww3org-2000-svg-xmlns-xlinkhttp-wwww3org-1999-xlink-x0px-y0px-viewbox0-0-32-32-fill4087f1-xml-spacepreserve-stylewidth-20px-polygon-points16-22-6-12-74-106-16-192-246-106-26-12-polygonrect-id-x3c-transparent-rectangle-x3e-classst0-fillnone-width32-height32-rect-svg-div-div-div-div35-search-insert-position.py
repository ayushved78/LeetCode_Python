class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
#         HOW DID THIS WORK??
        nums.append(float('inf'))
        begin_index, end_index = 0, len(nums) - 1
        while begin_index < end_index:
            mid = (begin_index+end_index) // 2
            if target <= nums[mid]:
                end_index = mid
            else:
                begin_index = mid + 1
                
        return begin_index