class Solution:
    def maximumHappinessSum(self, a: List[int], k: int) -> int:
        return sum(max(0,v-i) for i,v in enumerate(nlargest(k,a)))