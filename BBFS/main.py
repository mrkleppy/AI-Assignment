from collections import deque

GREEN = "\033[92m"
RESET = "\033[0m"

# Test datas
test_cases = [
    {
        "name": "Test data 1",
        "rows": 6,
        "cols": 7,
        "start": (0, 0),
        "end": (5, 6),
        "grid": [
            [1, 1, 0, 1, 1, 1, 1],
            [0, 1, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 1, 0, 1, 0],
            [1, 1, 0, 1, 1, 1, 1],
        ],
        "note": "Top Left Start, Bottom Right End, SAHC got solution"
    },
    {
        "name": "Test data 2",
        "rows": 7,
        "cols": 7,
        "start": (0, 6),
        "end": (6, 0),
        "grid": [
            [1, 1, 0, 1, 1, 1, 1],
            [1, 0, 1, 1, 0, 0, 1],
            [1, 1, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 0],
            [1, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 1],
        ],
        "note": "Top Right Start, Bottom Left End, SAHC got solution"
    },
    {
        "name": "Test data 3",
        "rows": 9,
        "cols": 8,
        "start": (8, 0),
        "end": (8, 7),
        "grid": [
            [1, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 1, 1, 0, 1],
            [1, 1, 0, 1, 1, 0, 1, 1],
            [0, 1, 0, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1],
            [0, 1, 1, 1, 1, 0, 0, 1],
            [1, 1, 0, 1, 0, 1, 1, 1],
        ],
        "note": "Bottom Left Start, Bottom Right End, SAHC no solution"
    },
    {
        "name": "Test data 4",
        "rows": 9,
        "cols": 9,
        "start": (8, 8),
        "end": (0, 0),
        "grid": [
            [1, 0, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 0, 0, 1, 1, 1, 0, 1],
            [0, 1, 1, 1, 0, 0, 1, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 0, 0, 1, 1, 0, 1],
            [1, 0, 1, 1, 0, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 0, 0, 1],
        ],
        "note": "Bottom Right Start, Top Left End, SAHC got solution"
    },
    {
        "name": "Test data 5",
        "rows": 10,
        "cols": 10,
        "start": (0, 9),
        "end": (0, 0),
        "grid": [
            [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
            [1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
            [0, 1, 1, 1, 1, 0, 0, 1, 0, 1],
            [0, 1, 0, 0, 1, 1, 1, 1, 0, 1],
            [1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        ],
        "note": "Top Right Start, Top Left End, SAHC no solution"
    },
    {
        "name": "Test data 6",
        "rows": 12,
        "cols": 11,
        "start": (11, 10),
        "end": (0, 10),
        "grid": [
            [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
            [0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
            [1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        ],
        "note": "Bottom Right Start, Top Right End, SAHC got solution, may need to change, DFS might find solution very fast too"
    },
    {
        "name": "Test data 7",
        "rows": 12,
        "cols": 13,
        "start": (11, 0),
        "end": (0, 12),
        "grid": [
            [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0],
            [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1],
            [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        ],
        "note": "Bottom Left Start, Top Right End, SAHC no solution"
    },
    {
        "name": "Test data 8",
        "rows": 14,
        "cols": 14,
        "start": (0, 0),
        "end": (13, 13),
        "grid": [
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
            [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ],
        "note": "Top Left Start, Bottom Right End, SAHC got solution, imperfect maze, many solutions, BFS and DFS time and space complexity will be interesting"
    },
    {
        "name": "Test data 9",
        "rows": 15,
        "cols": 15,
        "start": (14, 14),
        "end": (0, 0),
        "grid": [
            [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1],
            [1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        ],
        "note": "Bottom Right Start, Top Left End, SAHC no solution"
    },
    {
        "name": "Test data 10",
        "rows": 10,
        "cols": 10,
        "start": (0, 0),
        "end": (9, 9),
        "grid": [
            [1, 1, 0, 0, 1, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
            [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
            [0, 1, 1, 1, 1, 0, 0, 1, 0, 1],
            [1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        ],
        "note": "Top Left Start, Bottom Right End, control test data, intended to be impossible to solve"
    },
]

# Defining maze rules
class Maze:
    def __init__(self, mazeMap: list, end_row: int, end_column: int):
        self.mazeMap = mazeMap
        self.end_row = end_row
        self.end_column = end_column


class State:
    def __init__(self, current_row: int, current_column: int):
        self.current_row = current_row
        self.current_column = current_column
        self.parent = None

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


def successors(current_state, maze):
    children = []
    moves = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
    ]

    for move_row, move_column in moves:
        new_state = State(current_state.current_row + move_row, current_state.current_column + move_column)
        if new_state.is_valid(maze):
            new_state.parent = current_state
            children.append(new_state)

    return children

class BFS:
    def bfs(self, maze, start_row, start_column):
        start = State(start_row, start_column)
        goal = State(maze.end_row, maze.end_column)

        if not start.is_valid(maze) or not goal.is_valid(maze):
            print("Start or goal is invalid (wall or out of bounds).")
            return None

        from collections import deque

        queue = deque([(start, 0)])          # (state, level)
        visited = {start}
        parent_map = {start: None}          # for path reconstruction
        step = 0

        while queue:
            current, level = queue.popleft()
            step += 1

            # ---- Print expansion information ----
            print(f"\nStep {step}: \n")
            print(f"Expanded Node    : ({current.current_row}, {current.current_column})")

            # All valid neighbours (possible moves)
            all_moves = successors(current, maze)
            all_moves_coords = [(m.current_row, m.current_column) for m in all_moves]
            print(f"All Possible Moves    : {all_moves_coords}")

            # Add unvisited neighbours to the frontier
            added = []
            for child in all_moves:
                if child not in visited:
                    visited.add(child)
                    parent_map[child] = current
                    queue.append((child, level + 1))
                    added.append((child.current_row, child.current_column))
            print(f"Added to Frontier    : {added}")

            # Current frontier = all states currently in the queue
            frontier_coords = [(s.current_row, s.current_column) for s, _ in queue]
            print(f"Current Frontier    : {frontier_coords}")
            print(f"Frontier Size : {len(frontier_coords)}")

            # ---- Check goal ----
            if current == goal:
                # Reconstruct the path
                path = []
                node = current
                while node is not None:
                    path.append((node.current_row, node.current_column))
                    node = parent_map.get(node)
                path.reverse()

                # Print path in GREEN
                path_str = " -> ".join([f"({r},{c})" for r, c in path])
                print(f"\nPath found! Length: {len(path)}")
                print(f"Path: {GREEN}{path_str}{RESET}")

                return path

        # No path found
        print("\nNo path found from start to goal.")
        return None

# Bidrectional Breadth-First Search
class BidirectionalBFS:
    @staticmethod
    def bidirectional_bfs(maze, start_row, start_column):
        # Initialise the start and goal point
        start = State(start_row, start_column)
        goal = State(maze.end_row, maze.end_column)

        # queue for BFS from start and goal
        # deque is for efficient pop from left and append to right, for both the exit and start
        q_start = deque([start])
        q_goal = deque([goal])

        # visited sets for BFS from start and goal
        v_start = {start}
        v_goal = {goal}

        # parent dictionaries for BFS from start and goal to reconstruct the path
        p_start = {start: None}
        p_goal = {goal: None}

        while q_start and q_goal:
            # Since this is a bidirectional BFS, we will alternate between expanding the search from the start and the goal.
            # BFS from start
            current_start = q_start.popleft()
            for child in successors(current_start, maze):
                if child not in v_start:
                    # Add the child to the visited set, parent dictionary, and queue for BFS from start
                    v_start.add(child)
                    p_start[child] = current_start
                    q_start.append(child)

                    if child in v_goal:
                        # If the child is found in the goal's visited set, we reconstruct the path from start to goal
                        return BidirectionalBFS.construct_path(child, p_start, p_goal)

            # BFS from goal
            current_goal = q_goal.popleft()
            for child in successors(current_goal, maze):
                if child not in v_goal:
                    v_goal.add(child)
                    p_goal[child] = current_goal
                    q_goal.append(child)
                    if child in v_start:
                        # If the child is found in the start's visited set, we reconstruct the path from start to goal
                        return BidirectionalBFS.construct_path(child, p_start, p_goal)

        return None  # If no path is found, return none

    @staticmethod
    def construct_path(meet_state, p_start, p_goal):
        # Reconstruct the path from start to goal through the meeting point
        # First, reconstruct the path from start to meeting point
        path_start = []
        node = meet_state
        while node is not None:
            path_start.append((node.current_row, node.current_column))
            node = p_start.get(node)
        path_start.reverse()  # Reverses the path from start to meeting point to get the correct order from start to meeting point

        # Secondly, reconstruct the path from meeting point to goal
        path_goal = []
        node = p_goal.get(meet_state)
        while node is not None:
            path_goal.append((node.current_row, node.current_column))
            node = p_goal.get(node)

        return path_start + path_goal  # Constructs the path from start to goal through the meeting point

# SAHC
class HillClimbing:
    @staticmethod
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

    @staticmethod
    def apply_move(current_state, move):
        move_row, move_column = move
        new_state = State(
            current_state.current_row + move_row,
            current_state.current_column + move_column
        )
        return new_state

    @staticmethod
    def calculate_heuristic(current_state, maze):
        heuristic = abs(current_state.current_row - maze.end_row) + abs(current_state.current_column - maze.end_column)
        return heuristic

    @staticmethod
    def hillClimbing(initial_maze, initial_state):
        if initial_state.is_goal(initial_maze):
            return [initial_state]

        maze = initial_maze
        current_state = initial_state
        path = [current_state]
        heuristic = HillClimbing.calculate_heuristic(current_state, maze)
        level = 0
        visited = set()

        while heuristic > 0:
            print(f"\n---------")
            print(f"LEVEL  {level}")
            print(f"---------")
            print(f"CURRENT NODE: {current_state.current_row}, {current_state.current_column}, {heuristic}")

            visited.add(current_state)
            possible_moves = HillClimbing.get_possible_move(current_state, maze)

            if not possible_moves:
                print("No possible moves from current state")
                break

            next_states = []
            for move in possible_moves:
                new_state = HillClimbing.apply_move(current_state, move)
                new_heuristic = HillClimbing.calculate_heuristic(new_state, maze)
                next_states.append((new_state, new_heuristic))

            next_states.sort(key=lambda x: x[1])  # sort by heuristic ascending
            print("OPEN LIST:", [(s.current_row, s.current_column, h) for s, h in next_states])

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

# UI for running everything
def print_maze(maze_map):
    print("\nMaze:")
    for row in maze_map:
        colored_row = []
        for cell in row:
            if cell == 1:
                colored_row.append(f"{GREEN}{cell}{RESET}")
            else:
                colored_row.append(str(cell))
        print(" ".join(colored_row))
        
def main():
    while True:
        print("Enter 0 to exit or choose a test case number (1-10):")
        
        try:
            caseNo = int(input("Enter test case number: "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if caseNo == 0:
            print("Exiting program.\n")
            break
            
        if caseNo < 1 or caseNo > 10:
            print("Invalid test case number.\n")
            continue
            
        selected_case = test_cases[caseNo - 1]

        maze_map = selected_case["grid"]
        start_row, start_column = selected_case["start"]
        end_row, end_column = selected_case["end"]

        maze = Maze(maze_map, end_row, end_column)

        while True:
            print_maze(maze_map)

            print(f"\nStart: ({start_row}, {start_column}), End: ({end_row}, {end_column})")

            print("\n\tChoose an algorithm to run the test case:")
            print("\t\t1. Breadth-First Search")
            print("\t\t2. Depth-First Search")
            print("\t\t3. Bidirectional Breadth-First Search")
            print("\t\t4. A* Search")
            print("\t\t5. Hill Climbing")
            
            try:
                algorithmChoice = int(input("Enter algorithm choice (1-5): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if algorithmChoice == 0:
                break
            
            print_maze(maze_map)
            
            if algorithmChoice == 1:
                bfs = BFS()
                path = bfs.bfs(maze, start_row, start_column) # WIP
                print("\nBreadth-First Search Path:", path)
                input("\nPress Enter to return to the main menu...")

            elif algorithmChoice == 2:
                path = dfs(maze, start_row, start_column) # WIP
                print("\nDepth-First Search Path:", path)
                input("\nPress Enter to return to the main menu...")

            elif algorithmChoice == 3:
                path = BidirectionalBFS.bidirectional_bfs(maze, start_row, start_column)
                print("\nBidirectional Breadth-First Search Path:", path)
                input("\nPress Enter to return to the main menu...")

            elif algorithmChoice == 4:
                path = a_star(maze, start_row, start_column) # WIP
                print("\nA* Path:", path)
                input("\nPress Enter to return to the main menu...")

            elif algorithmChoice == 5:
                initial_state = State(start_row, start_column)
                path = HillClimbing.hillClimbing(maze, initial_state)

                if path is not None:
                    print("\nSteepest-Ascent Hill Climbing Path:", [(s.current_row, s.current_column) for s in path])
                else:
                    print("\nSteepest-Ascent Hill Climbing Path: No solution")
                input("\nPress Enter to return to the main menu...")
                
            else:
                print("Invalid algorithm choice.")
        
if __name__ == "__main__":
    main()