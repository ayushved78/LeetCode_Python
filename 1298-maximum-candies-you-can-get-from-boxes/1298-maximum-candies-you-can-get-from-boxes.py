class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        visited = [False] * n       # Track visited boxes
        has_key = [False] * n       # Track keys we have
        has_box = [False] * n       # Track boxes we have

        q = deque()
        for box in initialBoxes:
            has_box[box] = True
            if status[box] == 1:
                q.append(box)

        total_candies = 0

        while q:
            box = q.popleft()
            if visited[box]:
                continue
            visited[box] = True
            total_candies += candies[box]

            # Collect keys
            for k in keys[box]:
                has_key[k] = True
                if has_box[k] and not visited[k]:
                    q.append(k)

            # Collect new boxes
            for b in containedBoxes[box]:
                has_box[b] = True
                if status[b] == 1 or has_key[b]:
                    q.append(b)

        return total_candies