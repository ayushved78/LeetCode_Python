class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                code = deque()
                while stack[-1] != '[':
                    code.appendleft(stack.pop())
                stack.pop()
                num = deque()
                while stack and stack[-1].isdigit():
                    num.appendleft(stack.pop())
                stack.append(int(''.join(num)) * ''.join(code))
        return ''.join(stack) 