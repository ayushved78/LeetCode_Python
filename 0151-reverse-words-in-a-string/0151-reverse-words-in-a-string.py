class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        self.reverse(chars,0,len(chars)-1)
        start = 0
        for end in range(len(chars) + 1):
            if end == len(chars) or chars[end] == ' ':
                self.reverse(chars, start, end - 1)
                start = end + 1
        return self.cleanup(chars)
    
    def reverse(self, chars, left, right):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    
    def cleanup(self, chars):
        n = len(chars)
        i,j = 0,0
        while j < n:
            while j < n and chars[j] == ' ':
                j += 1
            while j < n and chars[j] != ' ':
                chars[i] = chars[j]
                i+=1
                j+=1
            while j<n and chars[j] == ' ':
                j+=1
            if j < n:
                chars[i] = ' '
                i += 1

        return ''.join(chars[:i])