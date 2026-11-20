class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        width = len(grid[0])
        height = len(grid)
        visited = set()
        islands = 0
        stack = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(height):
            for j in range(width):
                if grid[i][j] == "0" or (i,j) in visited:
                    continue
                
                visited.add((i,j))
                stack.append([i,j])
                islands += 1

                while stack:
                    row, col = stack.pop()

                    for dr, dc in directions:
                        r, c = row + dr, col + dc

                        if 0 <= r < height and 0<= c < width:
                            if grid[r][c] == "1" and (r,c) not in visited:
                                stack.append([r,c])
                                visited.add((r,c))
        return islands