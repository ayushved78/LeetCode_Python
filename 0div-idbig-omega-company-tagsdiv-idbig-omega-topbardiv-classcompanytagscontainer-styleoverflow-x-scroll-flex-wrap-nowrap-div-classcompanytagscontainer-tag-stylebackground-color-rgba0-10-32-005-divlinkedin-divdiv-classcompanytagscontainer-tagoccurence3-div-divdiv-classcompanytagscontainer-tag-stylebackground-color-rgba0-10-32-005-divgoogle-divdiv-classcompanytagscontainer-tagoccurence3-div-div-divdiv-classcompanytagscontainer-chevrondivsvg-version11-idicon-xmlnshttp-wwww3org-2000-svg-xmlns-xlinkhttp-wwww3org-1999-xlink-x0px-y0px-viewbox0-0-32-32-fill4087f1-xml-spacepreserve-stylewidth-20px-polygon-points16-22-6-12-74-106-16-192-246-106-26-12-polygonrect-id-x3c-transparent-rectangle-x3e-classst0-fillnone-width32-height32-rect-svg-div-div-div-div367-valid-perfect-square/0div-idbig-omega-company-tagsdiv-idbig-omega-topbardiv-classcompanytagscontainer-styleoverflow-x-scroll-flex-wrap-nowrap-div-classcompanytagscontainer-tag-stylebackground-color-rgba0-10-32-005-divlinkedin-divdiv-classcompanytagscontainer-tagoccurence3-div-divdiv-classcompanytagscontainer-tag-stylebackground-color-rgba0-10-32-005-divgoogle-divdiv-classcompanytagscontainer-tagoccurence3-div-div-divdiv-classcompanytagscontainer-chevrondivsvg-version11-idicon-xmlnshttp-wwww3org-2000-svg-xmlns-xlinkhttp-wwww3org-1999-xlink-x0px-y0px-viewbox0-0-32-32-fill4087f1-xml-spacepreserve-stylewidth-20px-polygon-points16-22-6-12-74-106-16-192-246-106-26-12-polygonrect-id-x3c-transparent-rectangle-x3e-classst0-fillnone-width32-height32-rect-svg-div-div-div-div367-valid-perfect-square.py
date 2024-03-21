class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return 1
        else:
            low = 1
            high = num / 2
            
            while low <= high:
                mid = (low+high) // 2
                guess = mid*mid
                if guess == num:
                    return mid
                elif guess > num:
                    high = mid - 1
                else:
                    low = mid + 1