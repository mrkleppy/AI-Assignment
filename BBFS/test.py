from Maze_generator import generate_maze
from Maze import Maze
from Bidirectional_BFS import bidirectional_bfs

rows, columns = 7,9
    
maze_map = generate_maze(rows, columns)
maze = Maze(maze_map, rows - 1, columns - 1)

path = bidirectional_bfs(maze, 0, 0)

GREEN = "\033[92m"
RESET = "\033[0m"

print("Maze: \n")
for row in maze_map:
    colored_row = []
    for cell in row:
        if cell == 1:
            colored_row.append(f"{GREEN}{cell}{RESET}")
        else:
            colored_row.append(str(cell))
    print(" ".join(colored_row))

if path:
    print("\nPath found: ")
    print(path)
else:
    print("\nNo path found.")