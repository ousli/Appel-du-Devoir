import random


def generate_maze(rows, columns):
    # Create a empty maze filled with "X" characters
    maze = [["X" for j in range(columns)] for i in range(rows)]

    # Fill the maze with " " characters to create a path through the maze
    for i in range(1, rows, 2):
        for j in range(1, columns, 2):
            maze[i][j] = " "

    # Randomly remove walls to create a path through the maze
    for i in range(2, rows - 1, 2):
        for j in range(2, columns - 1, 2):
            if random.random() > 0.5:
                maze[i][j] = " "
                maze[i + 1][j] = " "
            else:
                maze[i][j + 1] = " "
                maze[i + 1][j + 1] = " "

    return maze


def print_maze(maze):
    for row in maze:
        print(" ".join(row))


maze = generate_maze(20, 20)
print_maze(maze)
