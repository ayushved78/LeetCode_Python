class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        tmoves=0
        for i in range(len(seats)):
            tmoves+=abs(seats[i]-students[i])
        return tmoves