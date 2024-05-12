class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        result = 0
        want = sorted(nums)
        for _ in range(len(nums)):
            if want == nums:
                return result
            
            nums.insert(0, nums.pop())
            result += 1
        
        return -1