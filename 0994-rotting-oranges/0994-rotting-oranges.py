class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        grid_copy = deepcopy(grid)

        fresh_cnt = 0
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1

        minutes = 0
        while queue and fresh_cnt > 0:
            minutes += 1
            total_rottens = len(queue)
            for _ in range(total_rottens):
                i, j = queue.popleft()
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i, new_j = i + x, j + y
                    if new_i < 0 or new_i >= rows or new_j <0 or new_j >= cols:
                        continue 
                    if grid_copy[new_i][new_j] == 0 or grid_copy[new_i][new_j] == 2:
                        continue

                    fresh_cnt -= 1
                    grid_copy[new_i][new_j] = 2
                    queue.append((new_i, new_j))
        
        if fresh_cnt > 0:
            return -1
        return minutes