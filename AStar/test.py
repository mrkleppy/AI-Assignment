from Maze_generator import generate_maze
from Maze import Maze
from A_Star import AStar

GREEN = "\033[92m"
RESET = "\033[0m"

rows, columns = 7, 9

maze_map = generate_maze(rows, columns)
maze = Maze(maze_map, rows - 1, columns - 1)

print("Maze: \n")
for row in maze_map:
    colored_row = []
    for cell in row:
        if cell == 1:
            colored_row.append(f"{GREEN}{cell}{RESET}")
        else:
            colored_row.append(str(cell))
    print(" ".join(colored_row))

path = AStar(maze, 0, 0).a_star()
