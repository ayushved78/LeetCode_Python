class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # COPIED
        res = []
        def backTrack(i, cur_list, cur_sum):
            if cur_sum == target:
                res.append(cur_list.copy())
                return 
            if i >= len(candidates) or cur_sum > target:
                return
            cur_list.append(candidates[i])
            backTrack(i + 1, cur_list, cur_sum + candidates[i])
            cur_list.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backTrack(i + 1, cur_list, cur_sum)
        if candidates:
            candidates.sort()
        backTrack(0, [], 0)
        return res