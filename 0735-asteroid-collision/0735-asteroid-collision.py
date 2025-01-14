class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                # both asteroid explodes
                if abs(ast) > stack[-1]:
                    stack.pop()
                # equal asteroids explode
                elif abs(ast) == stack[-1]:
                    stack.pop()
                    break
                # all explode
                else:
                    break
            else:
                stack.append(ast)
        return stack
