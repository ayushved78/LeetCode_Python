class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = 0
        temp = x
        while temp > 0:
            ld = temp % 10
            res = res * 10 + ld
            temp = temp //10
        
        return res==x