class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s0 = students.count(0)
        s1 = students.count(1)
        
        for i in sandwiches:
            if i == 0 and s0 > 0:
                s0 -= 1
            elif i==1 and s1>0:
                s1 -= 1
            else:
                break
        
        return s0+s1