import random

def generate_maze(rows, columns):
    # Ensure that the number of rows and columns are odd to create a proper maze structure
    if rows % 2 == 0:
        rows += 1
    if columns % 2 == 0:
        columns += 1
    
    # Initialize the maze with walls (0) and paths (1) (Cannot go out of bounds)
    maze = [[0 for _ in range(columns)] for _ in range(rows)]
    
    # Start the maze generation from the top-left corner (1, 1) and mark it as a path
    start_row, start_column = 1, 1
    maze[start_row][start_column] = 1
    
    # Use stack to implement the BFS algorithm for maze generation
    stack = [(start_row, start_column)]
    
    # Define the possible directions to move in the maze (up, down, left, right)
    directions = [(-2, 0), (2,0), (0, -2), (0, 2)]
    
    # nr, nc = neighbor rows and columns
    # wr, wc = wall rows and columns
    # dr, dc = direction rows and columns
    
    while stack:
        # Get the current position from the top of the stack
        r, c = stack[-1]
        neighbours = []
        
        for dr, dc in directions:
            # Calculate the neighbour's row and column based on the current position and direction
            nr, nc = r + dr, c + dc
            
            # Check if the neighbour is within bounds and is a wall (0) to ensure we dont go out of bounds and only carve paths through walls
            if 1 <= nr < rows - 1 and 1 <= nc < columns - 1 and maze[nr][nc] == 0:
                neighbours.append((nr, nc, dr // 2, dc // 2))
        
        if neighbours:
            # Randomly select one of the unvisited neighbours to carve a path to
            nr, nc, wr, wc = random.choice(neighbours)
            
            # Carve a path to the selected neighbour by marking the wall and the neighbour as paths (1)
            maze[r + wr][c + wc] = 1
            
            # Mark the neighbour as a path (1) and add it to the stack to continue maze generation
            maze[nr][nc] = 1
            stack.append((nr, nc))
            
        else:
            stack.pop() # Backtrack if no unvisited neighbours are found
    
    
    # Set the start and goal positions in the maze to be paths (1) to ensure they are accesible
    maze[1][1] = 1 # Start point of the maze
    maze[rows - 2][columns - 2] = 1 # Exit point of the maze
    
    return maze