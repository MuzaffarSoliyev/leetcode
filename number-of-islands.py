import collections


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        self.rows, self.cols = len(grid), len(grid[0])
        self.visit = set()
        islands = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == '1' and (r, c) not in self.visit:
                    self.bfs(r, c, grid)
                    islands += 1
        return islands

    def bfs(self, r, c, grid):
        q = collections.deque
        self.visit.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(self.rows) and
                        c in range(self.cols) and
                        grid[r][c] == '1' and
                        (r, c) not in self.visit):
                    q.append((r, c))
                    self.visit.add((r, c))
