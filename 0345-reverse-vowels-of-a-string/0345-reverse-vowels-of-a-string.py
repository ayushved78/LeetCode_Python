class Solution:
    def reverseVowels(self, s: str) -> str:
        l,h = 0, len(s)-1
        vow = ['a','e','i','o','u','A','E','I','O','U']
        s_list = list(s)
        while l <= h:
            if s_list[l] not in vow:
                l += 1
            elif s_list[h] not in vow:
                h -= 1
            else:
                s_list[l], s_list[h] = s_list[h], s_list[l]
                l += 1
                h -= 1
        return ''.join(s_list)
