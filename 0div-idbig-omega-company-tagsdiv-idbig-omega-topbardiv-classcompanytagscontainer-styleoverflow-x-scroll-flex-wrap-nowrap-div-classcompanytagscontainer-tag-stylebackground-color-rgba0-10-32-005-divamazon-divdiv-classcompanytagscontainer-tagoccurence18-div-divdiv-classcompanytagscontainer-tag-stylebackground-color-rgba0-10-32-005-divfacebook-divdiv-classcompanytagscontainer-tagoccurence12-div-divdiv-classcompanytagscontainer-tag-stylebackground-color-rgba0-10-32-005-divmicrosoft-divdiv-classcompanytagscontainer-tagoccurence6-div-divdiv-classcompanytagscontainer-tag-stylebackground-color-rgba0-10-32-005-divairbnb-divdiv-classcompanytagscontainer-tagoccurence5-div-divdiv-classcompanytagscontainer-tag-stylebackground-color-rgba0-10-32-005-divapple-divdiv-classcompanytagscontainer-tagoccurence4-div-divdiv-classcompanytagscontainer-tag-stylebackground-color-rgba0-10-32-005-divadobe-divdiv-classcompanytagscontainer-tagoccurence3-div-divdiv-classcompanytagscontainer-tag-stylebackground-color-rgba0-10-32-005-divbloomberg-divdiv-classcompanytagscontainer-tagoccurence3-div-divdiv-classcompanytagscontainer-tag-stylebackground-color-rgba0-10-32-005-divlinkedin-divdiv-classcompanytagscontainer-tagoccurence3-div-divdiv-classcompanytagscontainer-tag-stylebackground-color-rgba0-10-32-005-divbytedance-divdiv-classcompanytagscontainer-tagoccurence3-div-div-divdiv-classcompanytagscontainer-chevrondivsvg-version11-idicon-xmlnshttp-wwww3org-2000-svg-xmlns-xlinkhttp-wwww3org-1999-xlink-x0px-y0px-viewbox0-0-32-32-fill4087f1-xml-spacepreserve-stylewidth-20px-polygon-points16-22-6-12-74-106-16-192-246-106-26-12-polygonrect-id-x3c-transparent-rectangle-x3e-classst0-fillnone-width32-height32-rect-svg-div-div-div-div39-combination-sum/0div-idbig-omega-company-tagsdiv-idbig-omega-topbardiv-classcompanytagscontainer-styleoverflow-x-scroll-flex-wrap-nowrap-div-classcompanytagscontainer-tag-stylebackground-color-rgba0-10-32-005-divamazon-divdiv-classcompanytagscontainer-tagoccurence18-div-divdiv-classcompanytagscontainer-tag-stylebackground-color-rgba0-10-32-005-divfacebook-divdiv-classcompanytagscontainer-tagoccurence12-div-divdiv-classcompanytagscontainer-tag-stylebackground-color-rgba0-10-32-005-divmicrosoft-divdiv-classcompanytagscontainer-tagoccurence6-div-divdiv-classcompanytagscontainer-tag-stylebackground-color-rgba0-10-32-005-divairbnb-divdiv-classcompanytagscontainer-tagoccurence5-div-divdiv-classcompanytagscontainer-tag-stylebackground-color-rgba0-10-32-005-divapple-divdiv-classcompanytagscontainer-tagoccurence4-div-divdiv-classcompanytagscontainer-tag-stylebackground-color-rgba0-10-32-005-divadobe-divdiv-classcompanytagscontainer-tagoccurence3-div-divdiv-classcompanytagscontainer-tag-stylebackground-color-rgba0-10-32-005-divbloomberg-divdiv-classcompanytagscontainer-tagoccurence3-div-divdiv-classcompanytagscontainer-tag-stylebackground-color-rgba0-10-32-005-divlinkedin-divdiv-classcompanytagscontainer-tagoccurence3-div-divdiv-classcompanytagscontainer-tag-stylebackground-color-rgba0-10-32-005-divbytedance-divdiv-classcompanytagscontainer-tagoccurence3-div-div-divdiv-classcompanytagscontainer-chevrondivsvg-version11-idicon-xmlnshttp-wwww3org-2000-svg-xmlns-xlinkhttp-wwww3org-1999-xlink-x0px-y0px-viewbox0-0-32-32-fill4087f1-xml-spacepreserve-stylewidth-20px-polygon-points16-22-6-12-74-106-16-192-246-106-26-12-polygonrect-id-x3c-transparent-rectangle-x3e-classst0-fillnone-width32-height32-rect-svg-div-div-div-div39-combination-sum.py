class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        def backtrack(i,cur):
            if i == len(candidates) or sum(cur) > target:
                return 
            if sum(cur) == target:
                res.append(cur.copy())
                return 
            cur.append(candidates[i])
            backtrack(i,cur)
            cur.pop()
            backtrack(i+1,cur)
        backtrack(0,[])
        return res