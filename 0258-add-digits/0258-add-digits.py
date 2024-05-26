class Solution:
    def addDigits(self, num: int) -> int:
        def sum(num):
            temp = num
            sum = 0
            while temp > 0:
                rem = temp % 10
                sum += rem
                temp = temp // 10
            return sum
        
        while num > 9:
            num = sum(num)
        return num