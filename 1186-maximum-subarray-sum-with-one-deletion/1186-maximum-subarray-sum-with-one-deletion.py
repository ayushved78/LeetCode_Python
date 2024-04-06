class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        @lru_cache(None)
        def dfs(i,delete):
            if i == n-1: return arr[i]
            if delete == 0: return max(dfs(i+1,delete)+arr[i],arr[i])
            return max(dfs(i+1,delete)+arr[i],dfs(i+1,delete-1),arr[i])

        return max([dfs(i,1) for i in range(n)])