class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            r_a = a%2
            r_b = b%2
            r_c = c%2
            if (r_a or r_b) != r_c:
                flips = flips + 1 + int(r_a and r_b)
                
            a = a//2
            b = b//2
            c = c//2
        return flips