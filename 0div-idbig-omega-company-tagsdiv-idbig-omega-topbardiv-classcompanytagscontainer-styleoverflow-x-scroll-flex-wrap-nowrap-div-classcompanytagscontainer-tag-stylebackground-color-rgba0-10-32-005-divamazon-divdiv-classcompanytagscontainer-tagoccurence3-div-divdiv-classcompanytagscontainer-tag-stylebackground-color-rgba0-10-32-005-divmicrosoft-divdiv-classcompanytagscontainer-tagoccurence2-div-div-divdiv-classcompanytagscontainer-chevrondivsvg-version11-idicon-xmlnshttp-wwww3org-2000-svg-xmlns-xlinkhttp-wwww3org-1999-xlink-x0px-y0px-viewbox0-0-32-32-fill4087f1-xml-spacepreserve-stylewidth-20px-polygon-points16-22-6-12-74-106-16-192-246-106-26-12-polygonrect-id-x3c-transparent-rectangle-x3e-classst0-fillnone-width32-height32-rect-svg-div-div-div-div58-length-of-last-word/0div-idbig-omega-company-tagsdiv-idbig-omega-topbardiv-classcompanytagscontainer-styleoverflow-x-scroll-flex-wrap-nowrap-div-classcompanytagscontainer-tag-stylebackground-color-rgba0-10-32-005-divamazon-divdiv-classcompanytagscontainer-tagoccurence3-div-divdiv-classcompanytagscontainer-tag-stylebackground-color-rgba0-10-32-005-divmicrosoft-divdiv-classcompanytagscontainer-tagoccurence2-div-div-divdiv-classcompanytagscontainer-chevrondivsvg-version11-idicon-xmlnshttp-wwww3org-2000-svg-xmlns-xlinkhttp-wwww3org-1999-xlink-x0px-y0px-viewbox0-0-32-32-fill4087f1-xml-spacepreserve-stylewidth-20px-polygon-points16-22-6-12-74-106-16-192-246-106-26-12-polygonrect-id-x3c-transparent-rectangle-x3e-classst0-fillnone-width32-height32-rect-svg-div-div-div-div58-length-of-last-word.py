class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        max_len = -1
        x=0
        for i in s:
            if i == " ":
                x = 0
                max_len = max(max_len,x)
            else:
                x+=1
        max_len = max(max_len, x)
        return max_len    