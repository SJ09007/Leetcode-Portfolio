class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        # Flatten the grid
        arr = []
        for row in grid:
            arr.extend(row)

        # Avoid unnecessary full rotations
        k %= (m * n)

        # Shift right by k
        arr = arr[-k:] + arr[:-k] if k else arr

        # Convert back to 2D grid
        return [arr[i:i+n] for i in range(0, m*n, n)]