# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:_COPIED

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first_bad = n
        start = 0
        end = n - 1

        while start <= end:
            mid = (start + end)//2
            if isBadVersion(mid):
                first_bad = mid
                end = mid - 1
            else:
                start = mid + 1

        return first_bad