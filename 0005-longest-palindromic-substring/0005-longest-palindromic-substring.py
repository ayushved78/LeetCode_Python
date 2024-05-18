class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l,r):
            nonlocal max_length, string
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if max_length < r-l+1:
                max_length = r-l+1
                string = s[l+1:r]

        max_length = 0 
        string = ""

        for i in range(len(s)):
            check(i,i)
            check(i,i+1)
        
        return string