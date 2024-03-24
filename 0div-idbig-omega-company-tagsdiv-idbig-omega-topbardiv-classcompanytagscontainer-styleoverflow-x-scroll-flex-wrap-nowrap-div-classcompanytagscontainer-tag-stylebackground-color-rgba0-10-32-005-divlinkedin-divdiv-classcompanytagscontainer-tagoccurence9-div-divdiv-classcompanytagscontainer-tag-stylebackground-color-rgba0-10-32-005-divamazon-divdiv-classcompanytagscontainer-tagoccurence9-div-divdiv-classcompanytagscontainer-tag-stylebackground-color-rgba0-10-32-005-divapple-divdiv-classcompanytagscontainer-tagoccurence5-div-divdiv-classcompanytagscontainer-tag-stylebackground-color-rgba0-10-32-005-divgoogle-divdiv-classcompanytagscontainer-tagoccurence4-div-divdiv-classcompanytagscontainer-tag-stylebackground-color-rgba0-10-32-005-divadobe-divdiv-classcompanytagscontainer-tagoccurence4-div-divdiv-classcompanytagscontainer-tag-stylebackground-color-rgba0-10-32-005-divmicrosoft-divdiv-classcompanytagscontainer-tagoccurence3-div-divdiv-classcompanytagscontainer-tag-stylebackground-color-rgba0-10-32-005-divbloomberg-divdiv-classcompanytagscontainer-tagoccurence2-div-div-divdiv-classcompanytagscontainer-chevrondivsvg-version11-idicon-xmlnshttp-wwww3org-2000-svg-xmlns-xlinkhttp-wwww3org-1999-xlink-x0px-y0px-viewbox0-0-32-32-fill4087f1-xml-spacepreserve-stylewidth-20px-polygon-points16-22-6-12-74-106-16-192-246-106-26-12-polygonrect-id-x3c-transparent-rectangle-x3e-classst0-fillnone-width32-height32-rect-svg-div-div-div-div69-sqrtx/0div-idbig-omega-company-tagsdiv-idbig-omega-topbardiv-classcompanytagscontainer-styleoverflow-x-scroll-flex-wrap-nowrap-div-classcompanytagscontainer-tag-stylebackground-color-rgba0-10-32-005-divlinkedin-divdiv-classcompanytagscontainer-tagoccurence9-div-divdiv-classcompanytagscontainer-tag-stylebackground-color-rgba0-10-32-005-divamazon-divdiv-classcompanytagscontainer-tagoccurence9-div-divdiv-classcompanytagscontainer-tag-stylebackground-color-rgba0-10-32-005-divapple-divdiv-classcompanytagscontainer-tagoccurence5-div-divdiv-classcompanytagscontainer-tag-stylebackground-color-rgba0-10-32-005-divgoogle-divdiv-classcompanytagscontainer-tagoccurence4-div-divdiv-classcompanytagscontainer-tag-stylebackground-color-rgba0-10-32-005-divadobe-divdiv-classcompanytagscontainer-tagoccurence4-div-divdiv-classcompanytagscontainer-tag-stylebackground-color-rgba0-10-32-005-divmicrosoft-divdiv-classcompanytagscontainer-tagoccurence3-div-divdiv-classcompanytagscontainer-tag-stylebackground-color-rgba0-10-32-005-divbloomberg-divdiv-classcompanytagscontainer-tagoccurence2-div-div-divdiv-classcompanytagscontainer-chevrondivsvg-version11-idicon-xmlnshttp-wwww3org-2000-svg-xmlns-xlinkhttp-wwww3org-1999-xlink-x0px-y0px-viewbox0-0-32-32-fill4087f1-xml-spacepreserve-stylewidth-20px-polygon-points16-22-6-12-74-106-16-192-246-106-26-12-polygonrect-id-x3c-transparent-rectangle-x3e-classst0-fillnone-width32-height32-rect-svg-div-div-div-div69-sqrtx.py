class Solution:
    def mySqrt(self, x: int) -> int:
#         SOLUTION 1 using math.pow()
        '''return int(pow(x,0.5))'''
#     SOLUTION 2 using binary search
        left = 0
        right = x
        while left <= right:
            mid = (left + right)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                left = mid + 1
            else:
                right = mid - 1
                
        return right