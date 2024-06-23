class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 == str2+str1:
            temp = str1 + str2
            size1 = len(str1)
            size2 = len(str2)

            if size1 < size2:
                size1, size2 = size2, size1

            for i in range(size2,0,-1):
                if size1 % i == 0 and size2 % i == 0:
                    return str1[:i]
    
        return ""