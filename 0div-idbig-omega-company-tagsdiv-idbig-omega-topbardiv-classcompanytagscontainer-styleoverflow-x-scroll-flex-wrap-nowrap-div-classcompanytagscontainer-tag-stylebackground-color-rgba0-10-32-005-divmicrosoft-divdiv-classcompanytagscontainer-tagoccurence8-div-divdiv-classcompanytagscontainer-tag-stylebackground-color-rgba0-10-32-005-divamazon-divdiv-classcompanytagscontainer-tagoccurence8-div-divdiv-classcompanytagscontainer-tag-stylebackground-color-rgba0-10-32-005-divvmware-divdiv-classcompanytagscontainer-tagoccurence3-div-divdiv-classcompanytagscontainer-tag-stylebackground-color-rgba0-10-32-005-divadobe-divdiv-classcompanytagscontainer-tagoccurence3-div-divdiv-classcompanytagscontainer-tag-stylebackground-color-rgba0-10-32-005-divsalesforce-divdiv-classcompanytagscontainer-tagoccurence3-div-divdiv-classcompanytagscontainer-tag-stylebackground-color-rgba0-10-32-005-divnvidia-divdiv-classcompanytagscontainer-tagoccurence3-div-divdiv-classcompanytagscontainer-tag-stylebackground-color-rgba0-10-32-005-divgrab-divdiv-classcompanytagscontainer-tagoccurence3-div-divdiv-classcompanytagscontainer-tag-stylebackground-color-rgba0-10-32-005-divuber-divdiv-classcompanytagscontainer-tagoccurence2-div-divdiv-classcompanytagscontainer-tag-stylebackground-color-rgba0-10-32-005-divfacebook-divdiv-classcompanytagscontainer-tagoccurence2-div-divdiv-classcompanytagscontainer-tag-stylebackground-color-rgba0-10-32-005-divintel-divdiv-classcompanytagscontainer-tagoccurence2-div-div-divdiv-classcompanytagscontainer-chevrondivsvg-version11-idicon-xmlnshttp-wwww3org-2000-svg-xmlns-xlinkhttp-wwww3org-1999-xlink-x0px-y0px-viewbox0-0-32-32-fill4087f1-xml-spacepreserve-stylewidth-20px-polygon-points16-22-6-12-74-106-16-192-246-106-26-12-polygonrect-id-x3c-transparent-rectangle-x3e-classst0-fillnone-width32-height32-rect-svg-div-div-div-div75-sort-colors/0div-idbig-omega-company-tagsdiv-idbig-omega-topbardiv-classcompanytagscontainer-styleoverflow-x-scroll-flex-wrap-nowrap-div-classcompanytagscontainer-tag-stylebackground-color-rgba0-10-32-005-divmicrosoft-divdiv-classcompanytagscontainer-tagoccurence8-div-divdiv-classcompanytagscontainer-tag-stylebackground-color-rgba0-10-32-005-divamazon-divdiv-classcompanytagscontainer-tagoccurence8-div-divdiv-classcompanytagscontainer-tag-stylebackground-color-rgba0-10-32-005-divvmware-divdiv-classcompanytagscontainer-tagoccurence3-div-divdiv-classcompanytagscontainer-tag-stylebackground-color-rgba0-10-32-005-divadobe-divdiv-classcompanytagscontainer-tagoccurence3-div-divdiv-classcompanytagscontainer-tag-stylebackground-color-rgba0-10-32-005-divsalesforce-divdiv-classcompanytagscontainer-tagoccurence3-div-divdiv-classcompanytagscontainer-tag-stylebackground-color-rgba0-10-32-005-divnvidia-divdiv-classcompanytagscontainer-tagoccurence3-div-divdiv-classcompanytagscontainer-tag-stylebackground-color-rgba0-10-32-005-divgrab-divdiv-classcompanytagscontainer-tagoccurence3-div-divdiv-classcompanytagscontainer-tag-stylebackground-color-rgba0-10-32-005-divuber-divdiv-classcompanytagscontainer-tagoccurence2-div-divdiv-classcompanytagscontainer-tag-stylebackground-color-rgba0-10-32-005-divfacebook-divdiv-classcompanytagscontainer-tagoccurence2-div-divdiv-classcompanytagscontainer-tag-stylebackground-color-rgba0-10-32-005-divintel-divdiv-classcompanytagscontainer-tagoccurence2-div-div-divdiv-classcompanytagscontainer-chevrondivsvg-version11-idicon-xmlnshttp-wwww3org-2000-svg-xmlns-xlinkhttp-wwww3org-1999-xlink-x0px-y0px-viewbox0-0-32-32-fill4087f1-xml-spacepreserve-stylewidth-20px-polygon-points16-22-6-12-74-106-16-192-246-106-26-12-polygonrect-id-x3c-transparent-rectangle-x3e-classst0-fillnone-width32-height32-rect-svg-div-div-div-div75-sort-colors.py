class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n
        while i!=0:
            for j in range(i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
            i-=1
        