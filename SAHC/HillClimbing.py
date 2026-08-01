class Maze:
    def __init__(self, mazeMap: list, end_row: int, end_column: int):
        self.mazeMap = mazeMap
        self.end_row = end_row
        self.end_column = end_column

class State:
    def __init__(self, current_row: int, current_column: int):
        self.current_row = current_row
        self.current_column = current_column

    def is_goal(self, maze):
        return self.current_row == maze.end_row and self.current_column == maze.end_column

    def is_valid(self, maze):     
        return (
            0 <= self.current_row < len(maze.mazeMap) and
            0 <= self.current_column < len(maze.mazeMap[0]) and
            maze.mazeMap[self.current_row][self.current_column] == 1
        )

    def __eq__(self, other):
        return self.current_row == other.current_row and self.current_column == other.current_column

    def __hash__(self):
        return hash((self.current_row, self.current_column))

def get_possible_move(current_state, maze):
    moves = []
    
    # Up
    up_state = State(current_state.current_row - 1, current_state.current_column)
    if up_state.is_valid(maze):
        moves.append((-1, 0))
    
    # Down
    down_state = State(current_state.current_row + 1, current_state.current_column)
    if down_state.is_valid(maze):
        moves.append((1, 0))
    
    # Left
    left_state = State(current_state.current_row, current_state.current_column - 1)
    if left_state.is_valid(maze):
        moves.append((0, -1))
    
    # Right
    right_state = State(current_state.current_row, current_state.current_column + 1)
    if right_state.is_valid(maze):
        moves.append((0, 1))
    
    return moves

def apply_move(current_state, move):
    move_row, move_column = move
    new_state = State(
        current_state.current_row + move_row,
        current_state.current_column + move_column
    )
    return new_state

def calculate_heuristic(current_state, maze):
    heuristic = abs(current_state.current_row - maze.end_row) + abs(current_state.current_column - maze.end_column)
    return heuristic
    
def hillClimbing(initial_maze, initial_state):
    if initial_state.is_goal(initial_maze):
        return [initial_state]
    
    maze = initial_maze
    current_state = initial_state
    path = [current_state]
    heuristic = calculate_heuristic(current_state, maze)
    level = 0
    visited = set()
    
    while heuristic > 0:
        print(f"\n---------")
        print(f"LEVEL  {level}")
        print(f"---------")
        print(f"CURRENT NODE: {current_state.current_row}, {current_state.current_column}, {heuristic}")
        
        visited.add(current_state)
        possible_moves = get_possible_move(current_state, maze)
        
        if not possible_moves:
            print("No possible moves from current state")
            break
        
        next_states = []
        for move in possible_moves:
            new_state = apply_move(current_state, move)
            new_heuristic = calculate_heuristic(new_state, maze)
            next_states.append((new_state, new_heuristic))
        
        next_states.sort(key=lambda x: x[1])  # sort by heuristic ascending
        print("OPEN LIST:", [( s.current_row, s.current_column, h ) for s, h in next_states])
        
        best_next_state, best_next_heuristic = next_states[0]
        
        if best_next_heuristic < heuristic and best_next_state not in visited:
            current_state = best_next_state
            heuristic = best_next_heuristic
            path.append(current_state)
            level += 1
            print("selected:", current_state.current_row, current_state.current_column, heuristic)
        else:
            print("there is no better move or already visited")
            print("\n ------------------------------------------------------------")
            print("Initial State:", initial_state.current_row, initial_state.current_column)
            print("Goal State:", maze.end_row, maze.end_column)
            print("Path:", [(s.current_row, s.current_column) for s in path])
            print("LOCAL MAXIMUM: There is no solution")
            return None
    
    print("\n ------------------------------------------------------------")
    print("Initial State:", initial_state.current_row, initial_state.current_column)
    print("Goal State:", maze.end_row, maze.end_column)
    print("Path:", [(s.current_row, s.current_column) for s in path])
    print("Solution Found!")
    return path