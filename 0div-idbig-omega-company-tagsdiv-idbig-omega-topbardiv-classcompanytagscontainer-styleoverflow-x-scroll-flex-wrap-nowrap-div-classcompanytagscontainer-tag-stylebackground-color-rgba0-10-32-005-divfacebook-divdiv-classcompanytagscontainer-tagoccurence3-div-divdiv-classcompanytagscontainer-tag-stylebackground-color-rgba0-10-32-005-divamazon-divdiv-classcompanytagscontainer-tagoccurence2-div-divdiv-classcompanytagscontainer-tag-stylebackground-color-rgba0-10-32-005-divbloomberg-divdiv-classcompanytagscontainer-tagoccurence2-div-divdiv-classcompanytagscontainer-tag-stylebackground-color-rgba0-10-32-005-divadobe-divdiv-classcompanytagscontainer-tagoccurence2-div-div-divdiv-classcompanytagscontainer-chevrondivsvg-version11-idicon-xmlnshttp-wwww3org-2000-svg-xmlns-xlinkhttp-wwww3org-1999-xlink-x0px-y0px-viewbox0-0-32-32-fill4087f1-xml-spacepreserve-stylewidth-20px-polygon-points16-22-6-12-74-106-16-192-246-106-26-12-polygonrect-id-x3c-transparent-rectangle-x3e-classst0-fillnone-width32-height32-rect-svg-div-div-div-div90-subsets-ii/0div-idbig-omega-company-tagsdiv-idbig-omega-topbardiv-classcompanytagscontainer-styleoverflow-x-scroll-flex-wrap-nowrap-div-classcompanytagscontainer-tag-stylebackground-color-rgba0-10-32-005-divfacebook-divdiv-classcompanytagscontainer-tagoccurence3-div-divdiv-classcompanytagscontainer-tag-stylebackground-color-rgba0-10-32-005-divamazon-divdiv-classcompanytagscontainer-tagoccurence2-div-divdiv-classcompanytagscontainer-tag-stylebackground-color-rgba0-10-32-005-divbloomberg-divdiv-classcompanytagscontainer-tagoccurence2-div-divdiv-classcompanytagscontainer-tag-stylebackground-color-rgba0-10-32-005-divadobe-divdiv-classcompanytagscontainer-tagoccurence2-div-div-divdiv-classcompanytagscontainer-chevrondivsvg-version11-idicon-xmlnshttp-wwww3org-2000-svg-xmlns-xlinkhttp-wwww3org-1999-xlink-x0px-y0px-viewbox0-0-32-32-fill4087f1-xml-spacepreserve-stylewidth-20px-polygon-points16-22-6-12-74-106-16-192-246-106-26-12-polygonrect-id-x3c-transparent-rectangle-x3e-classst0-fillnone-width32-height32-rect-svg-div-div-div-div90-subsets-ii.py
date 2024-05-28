class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        nums.sort()
        
        for i in nums:
            tmp = []
            for l in output:
                tmp.append(l+[i])
            output.extend(tmp)
            
        return [list(i) for i in set([tuple(i) for i in output])]