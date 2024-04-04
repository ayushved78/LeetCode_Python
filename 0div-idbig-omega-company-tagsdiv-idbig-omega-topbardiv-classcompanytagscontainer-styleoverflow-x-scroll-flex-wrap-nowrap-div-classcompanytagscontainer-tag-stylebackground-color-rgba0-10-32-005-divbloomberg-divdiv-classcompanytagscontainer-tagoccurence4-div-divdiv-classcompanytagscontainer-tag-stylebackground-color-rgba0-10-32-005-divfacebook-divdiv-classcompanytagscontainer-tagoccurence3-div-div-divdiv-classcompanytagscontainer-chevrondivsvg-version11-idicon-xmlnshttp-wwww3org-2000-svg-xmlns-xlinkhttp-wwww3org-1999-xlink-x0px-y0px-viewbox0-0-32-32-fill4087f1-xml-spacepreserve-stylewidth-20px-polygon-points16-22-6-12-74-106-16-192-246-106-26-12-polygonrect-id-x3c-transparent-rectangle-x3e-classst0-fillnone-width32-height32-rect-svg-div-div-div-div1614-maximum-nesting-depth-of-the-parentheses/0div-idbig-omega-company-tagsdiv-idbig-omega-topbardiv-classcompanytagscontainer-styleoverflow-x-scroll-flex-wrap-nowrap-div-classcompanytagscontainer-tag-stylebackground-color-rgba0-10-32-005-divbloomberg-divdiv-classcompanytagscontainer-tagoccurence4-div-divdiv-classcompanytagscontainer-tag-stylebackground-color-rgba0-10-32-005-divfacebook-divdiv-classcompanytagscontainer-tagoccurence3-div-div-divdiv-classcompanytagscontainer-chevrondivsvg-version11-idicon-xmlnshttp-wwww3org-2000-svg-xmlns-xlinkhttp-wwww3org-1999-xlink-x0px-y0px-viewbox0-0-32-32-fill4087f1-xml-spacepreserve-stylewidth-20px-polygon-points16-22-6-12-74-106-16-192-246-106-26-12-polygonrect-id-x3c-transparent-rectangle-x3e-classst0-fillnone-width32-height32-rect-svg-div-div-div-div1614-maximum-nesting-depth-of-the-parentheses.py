class Solution:
    def maxDepth(self, s: str) -> int:
        mx = 0
        depth = 0
        for x in s:
            if x == "(":
                depth += 1
                mx = max(mx,depth)
            elif x == ")":
                depth -= 1
                
        return mx