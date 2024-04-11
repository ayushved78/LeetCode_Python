class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k>0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
            
        stack = stack[:-k] if k > 0 else stack
        res = ''.join(stack).lstrip('0')
        return res if res else '0'