import heapq
from collections import deque
from itertools import count

GREEN = "\033[92m"
BLUE = "\033[0;34m"
RED = "\033[31m"
CYAN = "\033[0;36m"
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
            [1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
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

# Breadth-First Search
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

# Depth-First Search
class DepthFirstSearch():
    maxFrontier = 0
    numOfIteration = 0
    completed = False

    def dfs(self, maze, start_row, start_column):
        start = State(start_row, start_column)
        if start.is_goal(maze): return start

        frontier = [start] # DFS stack
        visited = {start} # stores non duplicate values. here, stores visited and rejecting duplicates
        current = start

        while frontier: # proceed if stack has nodes
            self.numOfIteration += 1

            current = frontier.pop(0) # get first element

            if current.is_goal(maze):
                self.completed = True
                return current

            visited.add(current)

            children = successors(current, maze)
            for child in children: # add tracing
                if child not in visited and child not in frontier:
                    frontier.insert(0, child)

                    if len(frontier) > self.maxFrontier: self.maxFrontier = len(frontier)

            trace = self.trace(start, maze, current, frontier, visited, children, self.completed)

        return current
        
    def trace(self, start, maze, current, frontier, visited, children, completed):
        print(f"============= Step {self.numOfIteration} =============")
        print(f"Current State: ({current.current_row}, {current.current_column})")
        print(f"Successors   : ", end = "")
        print(", ".join(f"({node.current_row}, {node.current_column})" for node in children), end="")
        print(f"\nFrontier     : ", end = "")
        print(", ".join(f"({node.current_row}, {node.current_column})" for node in frontier), end="")
        print(f"\nVisited      : ", end = "")
        print(", ".join(f"({node.current_row}, {node.current_column})" for node in visited), end="")
        print("\n")

    def construct_path(self, current, completed):
        
        if (completed == False):
            print("No solution has found")
            return []
        
        path = [current]
        self.parent = current.parent

        while self.parent:
            path.insert(0, self.parent)
            self.parent = self.parent.parent

        return path

    def result(self, path):
        print("========================== Result ==========================")
        print("Completeness                            : ", end = "")
        if self.completed: print("Completed")
        else: print("Incomplete (No solution has found)")
        print("Cost (Length of Path)                   :", len(path)) 
        print("Time Efficiency (Nodes Expanded)        :", self.numOfIteration)
        print("Space Efficiency (Max Nodes in Frontier):", self.maxFrontier)

# Bidrectional Breadth-First Search
class BidirectionalBFS:
    def __init__(self, maze, start_row, start_column):
        self.maze = maze
        self.start_row = start_row
        self.start_column = start_column
        self.number_of_expanded_nodes = 0
        self.maximum_frontier_size = 0
        self.completed = False
        self.final_meeting_state = None

    def bidirectional_bfs(self):
        # Initialise the start and goal point
        initial_state = State(self.start_row, self.start_column)
        goal_state = State(self.maze.end_row, self.maze.end_column)
    
        # queue for BFS from start and goal
        # deque is for efficient pop from left and append to right, for both the exit and start
        queue_from_initial = deque([initial_state])
        queue_from_goal = deque([goal_state])
    
        # visited sets for BFS from start and goal
        visited_from_start = {initial_state}
        visited_from_goal = {goal_state}
    
        # parent dictionaries for BFS from start and goal to reconstruct the path
        parent_from_initial = {initial_state: None}
        parent_from_goal = {goal_state: None}
    
        step_number = 0  # Step counter for showing the number of steps taken in the search
        self.maximum_frontier_size = len(queue_from_initial) + len(queue_from_goal)  # Space efficiency in practice: max total frontier size stored at one time
        meeting_state_object = None # The meeting point object where the two searches meet, used to reconstruct the path
    
        print("\nBidirectional Breadth-First Search")
        print("=" * 70)
    
        # The start and goal searches will continue until either one of the queues is empty or a meeting point is found
        while queue_from_initial and queue_from_goal:
            step_number += 1 # Increment the step counter for each iteration of the search
    
            # Since this is a bidirectional BFS, we will alternate between expanding the search from the start and the goal.
    
            # --------------------------------------------------- BFS from start ---------------------------------------------------
            current_state_from_initial = queue_from_initial.popleft() # LIFO: pop from left, FIFO: append to right
            self.number_of_expanded_nodes += 1 # Increment the number of expanded nodes for time complexity
    
            # Store coordinates for printing
            expanded_node = (
                current_state_from_initial.current_row,
                current_state_from_initial.current_column
            )
            all_possible_moves = []
            added_to_frontier = []
    
            # Generate successors for the current state from the initial search and process them
            for child_state in successors(current_state_from_initial, self.maze):
                child_position = (
                    child_state.current_row,
                    child_state.current_column
                )

                all_possible_moves.append(child_position)
    
                if child_state not in visited_from_start:
                    # Add the child to the visited set, parent dictionary, and queue for BFS from start
                    visited_from_start.add(child_state)
                    parent_from_initial[child_state] = current_state_from_initial
                    queue_from_initial.append(child_state)
    
                    # Store the added child position for printing
                    added_to_frontier.append(child_position)

                    # Calculate the current total frontier size by summing the lengths of both queues (For time efficiency and space efficiency)
                    current_total_frontier_size = len(queue_from_initial) + len(queue_from_goal)
    
                    # Update the maximum frontier size if the current total frontier size exceeds it
                    if current_total_frontier_size > self.maximum_frontier_size:
                        self.maximum_frontier_size = current_total_frontier_size
    
                    if child_state in visited_from_goal:
                        # If the child is found in the goal's visited set, we reconstruct the path from start to goal
                        self.final_meeting_state = child_position
                        meeting_state_object = child_state
                        self.completed = True
                        break
    
            # Store the current coordinates of the frontiers for printing
            start_frontier_coordinates = [
                (state.current_row, state.current_column)
                for state in queue_from_initial
            ]
            goal_frontier_coordinates = [
                (state.current_row, state.current_column)
                for state in queue_from_goal
            ]
    
            # Prints the current step information, including expanded nodes, all possible moves, added frontier nodes, and the current state of the frontiers for both searches
            self.trace(step_number, "Start Search", expanded_node, all_possible_moves, added_to_frontier, start_frontier_coordinates, goal_frontier_coordinates)
    
            if self.final_meeting_state is not None:
                break
    
            # --------------------------------------------------- BFS from goal ---------------------------------------------------
            current_state_from_goal = queue_from_goal.popleft()
            self.number_of_expanded_nodes += 1
    
            expanded_node = (
                current_state_from_goal.current_row,
                current_state_from_goal.current_column
            )
    
            all_possible_moves = []
            added_to_frontier = []
    
            for child_state in successors(current_state_from_goal, self.maze):
                child_position = (
                    child_state.current_row,
                    child_state.current_column
                )
    
                all_possible_moves.append(child_position)
    
                if child_state not in visited_from_goal:
                    # Add the child to the visited set, parent dictionary, and queue for BFS from goal
                    visited_from_goal.add(child_state)
                    parent_from_goal[child_state] = current_state_from_goal
                    queue_from_goal.append(child_state)
    
                    added_to_frontier.append(child_position)
    
                    current_total_frontier_size = len(queue_from_initial) + len(queue_from_goal)
    
                    if current_total_frontier_size > self.maximum_frontier_size:
                        self.maximum_frontier_size = current_total_frontier_size
    
                    if child_state in visited_from_start:
                        # If the child is found in the start's visited set, we reconstruct the path from start to goal
                        self.final_meeting_state = child_position
                        meeting_state_object = child_state
                        self.completed = True
                        break
    
            start_frontier_coordinates = [
                (state.current_row, state.current_column)
                for state in queue_from_initial
            ]
            goal_frontier_coordinates = [
                (state.current_row, state.current_column)
                for state in queue_from_goal
            ]
    
            # Prints the current step information, including expanded nodes, all possible moves, added frontier nodes, and the current state of the frontiers for both searches
            self.trace(step_number, "Goal Search", expanded_node, all_possible_moves, added_to_frontier, start_frontier_coordinates, goal_frontier_coordinates)
    
            # If a meeting point is found, we break out of the loop to reconstruct the path
            if self.final_meeting_state is not None:
                break
    
        # If a meeting point is found, we reconstruct the path from start to goal through the meeting point
        if self.final_meeting_state is not None:
            path = self.construct_path(
                meeting_state_object,
                parent_from_initial,
                parent_from_goal
            )
            self.result(path)
            return path
    
        #If no meeting point is found, we print no path was found and return None
        self.result(None)
        return None

    # For printing the details of each steps in the bidirectional BFS search
    def trace(self, step_number, direction, expanded_node, all_possible_moves, added_to_frontier, start_frontier_coordinates, goal_frontier_coordinates):
        # Color coding Start Search for better visualisation
        if direction == "Start Search":
            direction_color = GREEN
            start_frontier_label = f"{RED}Start Frontier{RESET}"
            goal_frontier_label = "Goal Frontier"
        else:
            direction_color = BLUE
            start_frontier_label = "Start Frontier"
            goal_frontier_label = f"{RED}Goal Frontier{RESET}"
            
        print(f"\n+----------------- Step {step_number}: From the {direction_color}{direction}{RESET} ------------------+")
        print(f"| Expanded Node       : {expanded_node}")
        print(f"| All Possible Moves  : {all_possible_moves}")
        print(f"| Added to Frontier   : {added_to_frontier}")
        print(f"| {start_frontier_label}      : {start_frontier_coordinates}")
        print(f"| {goal_frontier_label}       : {goal_frontier_coordinates}")
        print(f"| Total Frontier Size : {len(start_frontier_coordinates) + len(goal_frontier_coordinates)}")
        print("+------------------------------------------------------------------+")
        
    # For printing the final results of the bidirectional BFS search
    def result(self, path):
        print("\n" + "=" * 70)
        print("Bidirectional Breadth-First Search Results")
        print()
        
        # 
        if self.completed and path is not None:
            print(f"Completeness                             : {GREEN}Completed{RESET}")
            print("Meeting Point                            :", self.final_meeting_state)
            print("Cost (Length of Path)                    :", len(path))
            print("Bidirectional Breadth-First Search Path  :", path)
            
        else:
            print(f"Completeness                             : {RED}Not Complete (No solution has found){RESET}")
            print("Meeting Point                            : None")  
              
        print("Time Efficiency (Nodes Expanded)         :", self.number_of_expanded_nodes)
        print("Space Efficiency (Maximum Frontier Size) :", self.maximum_frontier_size)
        
    # For reconstructing the path from start to goal through the meeting point
    def construct_path(self, meeting_state, parent_from_initial, parent_from_goal):
        # Reconstruct the path from start to goal through the meeting point
        # First, reconstruct the path from start to meeting point
        path_from_start = []
        current_node = meeting_state
        while current_node is not None:
            path_from_start.append((current_node.current_row, current_node.current_column))
            current_node = parent_from_initial.get(current_node)
        path_from_start.reverse()  # Reverses the path from start to meeting point to get the correct order from start to meeting point

        # Secondly, reconstruct the path from meeting point to goal
        path_from_goal = []
        current_node = parent_from_goal.get(meeting_state)
        while current_node is not None:
            path_from_goal.append((current_node.current_row, current_node.current_column))
            current_node = parent_from_goal.get(current_node)

        return path_from_start + path_from_goal  # Constructs the path from start to goal through the meeting point

# A*
class AStar:
    # Initialise for the A* search
    def __init__(self, maze, start_row, start_column):
        # Store the maze and work out the start and goal states
        self.maze = maze
        self.start = State(start_row, start_column)
        self.goal = State(maze.end_row, maze.end_column)

        # counter is used to break ties in the heap so two states are never compared directly
        self.counter = count()
        # g_score keeps the best known cost from start to each state found so far
        self.g_score = {self.start: 0}
        # open_heap is the priority frontier, ordered by f = g + h
        self.open_heap = [(self.heuristic(self.start), next(self.counter), self.start)]
        # closed holds every state that has already been expanded
        self.closed = set()

        # stats used later to print the result summary
        self.step = 0
        self.max_frontier = 1
        self.completed = False

    # Calculate the heuristic value by performing manhattan distance
    def heuristic(self, state):
        return abs(state.current_row - self.maze.end_row) + abs(state.current_column - self.maze.end_column)

    # A* search algorithm
    def a_star(self):
        # If the start or goal is a wall or out of bounds then end
        if not self.start.is_valid(self.maze) or not self.goal.is_valid(self.maze):
            print("Start or goal is invalid (wall or out of bounds).")
            return None

        # Keep expanding the frontier until it is empty or the goal is found
        while self.open_heap:
            # Take the state with the lowest f score from the frontier
            f, _, current = heapq.heappop(self.open_heap)

            # Skip this entry if it was already expanded through a better path
            if current in self.closed:
                continue

            # Mark the state as expanded and record its scores
            self.closed.add(current)
            self.step += 1
            g = self.g_score[current]
            h = self.heuristic(current)

            print(f"\n+----------------- Step {self.step}: {CYAN}A* Search{RESET} ------------------+")
            print(f"| Expanded Node       : {CYAN}({current.current_row}, {current.current_column}){RESET}   g={g} h={h} f={f}")

            # If the current state is the goal then build and show the path
            if current.is_goal(self.maze):
                print("+------------------------------------------------------------------+")
                self.completed = True
                path = self.construct_path(current)
                self.result(path)
                return path

            # Find all valid neighbours of the current state
            children = successors(current, self.maze)  # child.parent is already set to current
            self.trace(children, g)

        # Frontier is empty and the goal was never reached
        self.result(None)
        return None

    # Print the step details and add the neighbours to the frontier
    def trace(self, children, g):
        relaxed = []
        for child in children:
            # The cost to reach a neighbour is always one more step than the current state
            tentative_g = g + 1
            # Only keep this neighbour if it is new, or the path found to it is better than before
            if child not in self.g_score or tentative_g < self.g_score[child]:
                self.g_score[child] = tentative_g
                f_child = tentative_g + self.heuristic(child)
                heapq.heappush(self.open_heap, (f_child, next(self.counter), child))
                relaxed.append((child.current_row, child.current_column, tentative_g, self.heuristic(child), f_child))

        # Update the largest frontier size seen so far, for the space efficiency stat
        self.max_frontier = max(self.max_frontier, len(self.open_heap))

        # Build a list of the states still waiting in the frontier, sorted by f score
        open_preview = sorted(
            (
                (s.current_row, s.current_column, sg, self.heuristic(s), sg + self.heuristic(s))
                for s, sg in self.g_score.items()
                if s not in self.closed
            ),
            key=lambda t: t[4]
        )

        print(f"| Possible Moves      : {[(c.current_row, c.current_column) for c in children]}")
        print(f"| Relaxed / Added     : {relaxed}")
        print(f"| Open List (f-sorted): {open_preview}")
        print(f"| Frontier Size       : {len(open_preview)}")
        print("+------------------------------------------------------------------+")

    # Reconstruct the path from goal back to start
    def construct_path(self, current):
        path = []
        node = current
        # Walk backwards using the parent of each state until reaching the start
        while node is not None:
            path.append((node.current_row, node.current_column))
            node = node.parent
        path.reverse()  # reverse so the path goes from start to goal

        path_str = " -> ".join(f"({r},{c})" for r, c in path)
        print(f"\nPath found! Length: {len(path)}")
        print(f"Path: {GREEN}{path_str}{RESET}")
        return path

    # Print out the completeness, cost, time and space of the search
    def result(self, path):
        print(f"\n{CYAN}========================== Result =========================={RESET}")
        print("Completeness                            : ", end="")
        if self.completed:
            # search reached the goal
            print(f"{GREEN}Completed{RESET}")
        else:
            # frontier ran out before reaching the goal
            print(f"{RED}Not Complete (No solution has found){RESET}")

        if path is not None:
            print("Cost (Length of Path)                   :", len(path))
        print("Time Efficiency (Nodes Expanded)        :", self.step)
        print("Space Efficiency (Max Nodes in Frontier):", self.max_frontier)


# SAHC
class SAHC:
    # Initialise for the SAHC
    def __init__(self, initial_maze, initial_state):
        self.maze = initial_maze
        self.current_state = initial_state
        self.path = [self.current_state]
        self.visited = set()
        self.level = 0
        self.heuristic = self.calculate_heuristic(self.current_state, self.maze)

    # SAHC serach Algorithm
    def SAHC(self):
        # if the start is goal then end
        if self.current_state.is_goal(self.maze):
            return [self.current_state]

        # Print out the process of each level
        while self.heuristic > 0:
            print("\n---------")
            print(f"LEVEL {self.level}")
            print("---------")
            print( # current position
                f"CURRENT NODE: {self.current_state.current_row}, "
                f"{self.current_state.current_column}, {self.heuristic}"
            )

            # Add the current state to visited to prevent going back
            self.visited.add(self.current_state)
            # Find all possible moves of current state
            possible_moves = self.get_possible_move(self.current_state, self.maze)

            # If no possible moves is found then end
            if not possible_moves:
                print("No possible moves from current state")
                break
            
            # Find all the next state of all the possible moves
            next_states = []
            for move in possible_moves:
                new_state = self.apply_move(self.current_state, move) # apply the move to find the next state
                new_heuristic = self.calculate_heuristic(new_state, self.maze) # find the heuristic value of the next state
                next_states.append((new_state, new_heuristic)) # add into the list

            # rearrange the next state list with the heuristic value in ascending order
            next_states.sort(key=lambda x: x[1])
            print("OPEN LIST:", [ # print out the oen list
                (state.current_row, state.current_column, heuristic)
                for state, heuristic in next_states
            ])

            # The best next state will be the next state with lowest heuristic value
            # After sorting the next state with lowest heuristic value will be at the front of the list
            best_next_state, best_next_heuristic = next_states[0]

            # Compare to check the best next state's heuristic value is lower than current state's heuristic value
            # Verify the best next state is not visited before
            if best_next_heuristic < self.heuristic and best_next_state not in self.visited:
                # Change the current state to the best next state to perform the move
                self.current_state = best_next_state
                self.heuristic = best_next_heuristic
                self.path.append(self.current_state) # store as the path chosen
                self.level += 1 # Proceed to next level
                # print the choice
                print("selected:", self.current_state.current_row, self.current_state.current_column, self.heuristic)
            else:
                # No better path to proceed, show the details
                print("there is no better move or already visited")
                print("\n ------------------------------------------------------------")
                print("Initial State:", self.path[0].current_row, self.path[0].current_column)
                print("Goal State:", self.maze.end_row, self.maze.end_column)
                print("Path:", [(state.current_row, state.current_column) for state in self.path])
                print("LOCAL MAXIMUM: There is no solution")
                return None

        # print out all the data
        print("\n ------------------------------------------------------------")
        print("Initial State:", self.path[0].current_row, self.path[0].current_column)
        print("Goal State:", self.maze.end_row, self.maze.end_column)
        print("Path:", [(state.current_row, state.current_column) for state in self.path])
        print("Solution Found!")
        return self.path

    def get_possible_move(self, current_state, maze):
        # Find every move that is valid in the current state (up, down, left and right)
        moves = []

        # Move upward, deduct the current state row by 1
        up_state = State(current_state.current_row - 1, current_state.current_column)
        if up_state.is_valid(maze):
            moves.append((-1, 0))
        
        # Move downward, add the current state row by 1
        down_state = State(current_state.current_row + 1, current_state.current_column)
        if down_state.is_valid(maze):
            moves.append((1, 0))

        # Move left, deduct the current state column by 1
        left_state = State(current_state.current_row, current_state.current_column - 1)
        if left_state.is_valid(maze):
            moves.append((0, -1))

        # Move right, add the current state column by 1
        right_state = State(current_state.current_row, current_state.current_column + 1)
        if right_state.is_valid(maze):
            moves.append((0, 1))

        return moves

    def apply_move(self, current_state, move):
        # perform all the moves that is passed in
        move_row, move_column = move
        return State(
            current_state.current_row + move_row,
            current_state.current_column + move_column
        )

    def calculate_heuristic(self, current_state, maze):
        # calculate the heuristic value by performing mamanhattan algorithm distance
        return abs(current_state.current_row - maze.end_row) + abs(current_state.current_column - maze.end_column)

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
      
# The maze path with solutions in them  
def print_maze_with_path(maze_map, path):
    print("\nMaze with Path Highlighted:")
    path_coordinates = set(path)

    for row_index, row in enumerate(maze_map):
        colored_row = []
        for column_index, cell in enumerate(row):
            current_position = (row_index, column_index)

            if current_position in path_coordinates:
                colored_row.append(f"{RED}{cell}{RESET}")
            elif cell == 1:
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
                algorithmChoice = int(input("Enter 0 to exit or choose an algorithm choice (1-5): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if algorithmChoice == 0:
                break
            
            if algorithmChoice == 1:
                path = BFS().bfs(maze, start_row, start_column)
                
                if path is not None:
                    print_maze_with_path(maze_map, path)
                else:
                    print("\nBreadth-First Search Path: No solution")
                    
                input("\nPress Enter to return to the main menu...")

            elif algorithmChoice == 2:
                dfs_solver = DepthFirstSearch()
                path = dfs_solver.dfs(maze, start_row, start_column)
                
                if dfs_solver.completed and path is not None:
                    dfs_solver.result(dfs_solver.construct_path(path, completed=dfs_solver.completed))
                    print("\nPath: ", end="")
                    print(", ".join(f"({s.current_row},{s.current_column})" for s in dfs_solver.construct_path(path, completed=dfs_solver.completed)))
                    print("")
                    print_maze_with_path(maze_map, [(s.current_row, s.current_column) for s in dfs_solver.construct_path(path, completed=dfs_solver.completed)])
                else:
                    print("\nDepth-First Search Path: No solution")
                    
                input("\nPress Enter to return to the main menu...")

            elif algorithmChoice == 3:
                bidirectional_bfs_solver = BidirectionalBFS(maze, start_row, start_column)
                path = bidirectional_bfs_solver.bidirectional_bfs()
                
                if path is not None:
                    print_maze_with_path(maze_map, path)
                else:
                    print("\nBidirectional Breadth-First Search Path: No solution")
                
                input("\nPress Enter to return to the main menu...")

            elif algorithmChoice == 4:
                A_Star_solver = AStar(maze, start_row, start_column)
                path = A_Star_solver.a_star()
                
                if path is not None:
                    print_maze_with_path(maze_map, path)
                    print("\nA* Path:", path)
                else:
                    print("\nA* Path: No solution")

                input("\nPress Enter to return to the main menu...")

            elif algorithmChoice == 5:
                initial_state = State(start_row, start_column)
                sahc = SAHC(maze, initial_state)
                path = sahc.SAHC()

                if path is not None:
                    print_maze_with_path(maze_map, [(s.current_row, s.current_column) for s in path])
                else:
                    print("\nSteepest-Ascent Hill Climbing Path: No solution")
                input("\nPress Enter to return to the main menu...")
                
            else:
                print("Invalid algorithm choice.")
        
if __name__ == "__main__":
    main()