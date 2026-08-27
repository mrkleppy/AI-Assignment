import random

def generate_maze(rows, columns, extra_openings=0.25):
    maze = [[0 for _ in range(columns)] for _ in range(rows)]

    start_row, start_column = 0, 0
    maze[start_row][start_column] = 1

    stack = [(start_row, start_column)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # First phase: generate a connected maze structure
    while stack:
        r, c = stack[-1]
        neighbours = []

        random.shuffle(directions)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < columns and maze[nr][nc] == 0:
                open_neighbours = 0

                for rr, cc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ar, ac = nr + rr, nc + cc
                    if 0 <= ar < rows and 0 <= ac < columns and maze[ar][ac] == 1:
                        open_neighbours += 1

                if open_neighbours <= 1:
                    neighbours.append((nr, nc))

        if neighbours:
            nr, nc = random.choice(neighbours)
            maze[nr][nc] = 1
            stack.append((nr, nc))
        else:
            stack.pop()

    # Ensure start and goal are open
    maze[0][0] = 1
    maze[rows - 1][columns - 1] = 1

    # Second phase: make maze imperfect by opening more blocked cells
    blocked_cells = [
        (r, c)
        for r in range(1, rows - 1)
        for c in range(1, columns - 1)
        if maze[r][c] == 0
    ]

    random.shuffle(blocked_cells)

    openings_to_add = int(len(blocked_cells) * extra_openings)

    for i in range(openings_to_add):
        r, c = blocked_cells[i]
        maze[r][c] = 1

    return maze