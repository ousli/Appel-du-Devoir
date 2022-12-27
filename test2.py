import random

# Constants
WALL = "#"
SPACE = " "
START = "S"
END = "E"

# Size of the maze
width = 10
height = 10

# Initialize the maze with walls
maze = []
for i in range(height):
    row = []
    for j in range(width):
        row.append(WALL)
    maze.append(row)

# Choose a starting position
start_x = random.randint(0, width - 1)
start_y = random.randint(0, height - 1)

# Initialize the stack with the starting position
stack = [(start_x, start_y)]

# Main loop
while stack:
    # Get the current position
    x, y = stack[-1]

    # Mark the current position as part of the maze
    maze[y][x] = SPACE

    # Get the neighbors of the current position
    neighbors = []
    if x > 0 and maze[y][x - 1] == WALL:
        neighbors.append((x - 1, y))
    if x < width - 1 and maze[y][x + 1] == WALL:
        neighbors.append((x + 1, y))
    if y > 0 and maze[y - 1][x] == WALL:
        neighbors.append((x, y - 1))
    if y < height - 1 and maze[y + 1][x] == WALL:
        neighbors.append((x, y + 1))

    # If there are no neighbors, backtrack
    if not neighbors:
        stack.pop()
    # If there are neighbors, choose one at random and add it to the stack
    else:
        stack.append(random.choice(neighbors))

# Choose an ending position
end_x = random.randint(0, width - 1)
end_y = random.randint(0, height - 1)

# Mark the ending position
maze[end_y][end_x] = END

# Print the maze
for row in maze:
    print(row)
