class Solution:
    def maxArea(self, height: List[int]) -> int:
        # assign 2 pointers and max_area
        l = 0
        r = len(height)-1
        max_area = float('-inf')
        # iterate till l<r
        while l < r:
            # area is nothing but min of l,r and difference of pointers to calculate blocks
            area = min(height[l],height[r]) * (r-l)
            # max area would be the max of area and max_area
            max_area = max(area, max_area)
            # increase/decrease pointer if h[l] < h[r]
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        # return the max area booked
        return max_area