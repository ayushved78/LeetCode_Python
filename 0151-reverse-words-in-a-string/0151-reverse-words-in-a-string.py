class Solution:
    def reverseWords(self, s: str) -> str:
        l:str = s.split()
        l.reverse()
        return ' '.join(l)