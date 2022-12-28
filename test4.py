from random import shuffle


def generate_maze(grid, r, c):
    # Shuffle the directions to visit cells randomly
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    shuffle(directions)

    for dx, dy in directions:
        new_r, new_c = r + dx, c + dy
        if (0 <= new_r < len(grid) and 0 <= new_c < len(grid[0])
                and grid[new_r][new_c] == 1):
            grid[r][c] = 0
            grid[new_r][new_c] = 0
            generate_maze(grid, new_r, new_c)


# Example usage
grid = [[1 for _ in range(10)] for _ in range(10)]
generate_maze(grid, 0, 0)

for row in grid:
    print(row)
