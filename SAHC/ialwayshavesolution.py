from Maze_generator import generate_maze
from SAHC.HillClimbing import hillClimbing, Maze, State

rows, columns = 14, 14

# row is top (0) or bottom (-1), column is left (0) or right (-1)
path = None
attempt = 0

while path is None:
    attempt += 1
    print(f"\nGenerating maze attempt {attempt}...")

    maze_map = generate_maze(rows, columns)
    maze = Maze(maze_map, rows - 1, columns - 1)
    initial_state = State(0, 0)

    path = hillClimbing(maze, initial_state)

GREEN = "\033[92m"
RESET = "\033[0m"

print("\nSolved Maze:\n")
for row in maze_map:
    colored_row = []
    for cell in row:
        if cell == 1:
            colored_row.append(f"{GREEN}{cell}{RESET}")
        else:
            colored_row.append(str(cell))
    print(" ".join(colored_row))

if path:
    print(f"\nPath found after {attempt} attempt(s):")
    print([(state.current_row, state.current_column) for state in path])
else:
    print("\nNo path found.")