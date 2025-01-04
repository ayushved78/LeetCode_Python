class Solution:
    def gcd(self, val1, val2):
        if val2 == 0:
            return abs(val1)
        else:
            return gcd(val2, val1 % val2)
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        size1 = len(str1)
        size2 = len(str2)
        gcd_len = self.gcd(size1,size2)
        candidate = str1[:gcd_len]
        if candidate * (size1 // gcd_len) == str1 and candidate * (size2 // gcd_len) == str2:
            return candidate
        
        return ""