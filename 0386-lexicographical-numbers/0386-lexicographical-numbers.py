class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        cur = 1

        for _ in range(n):
            result.append(cur)

            if cur * 10 <= n:
                cur*=10
            elif cur % 10 != 9 and cur + 1 <= n:
                cur+=1
            else:
                while (cur // 10) % 10 == 9:
                    cur //= 10
                cur = cur // 10 + 1

        return result