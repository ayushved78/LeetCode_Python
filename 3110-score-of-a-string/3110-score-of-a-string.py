class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(1,n):
            ans += abs(ord(s[i-1]) - ord(s[i]))
        return ans