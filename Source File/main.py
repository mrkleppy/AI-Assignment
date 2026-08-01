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

# Bidrectional Breadth-First Search
class BidirectionalBFS:
<<<<<<< HEAD
    def bidirectional_bfs(self, maze, start_row, start_column):
        # Initialise the start and goal point
        initial_state = State(start_row, start_column)
        goal_state = State(maze.end_row, maze.end_column)

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

        print("\nBidirectional Breadth-First Search\n")
        print(f"{'Step':<6} {'Direction':<10} {'Expanded Node':<18} {'Frontier':<30} {'Meeting State':<18}")

        while queue_from_initial and queue_from_goal:
            # Since this is a bidirectional BFS, we will alternate between expanding the search from the start and the goal.

            # BFS from start
            current_state_from_initial = queue_from_initial.popleft()
            step_number += 1

            expanded_node = (current_state_from_initial.current_row, current_state_from_initial.current_column)
            meeting_state = "-"

            frontier_updates = []

            for child_state in successors(current_state_from_initial, maze):
                if child_state not in visited_from_start:
                    # Add the child to the visited set, parent dictionary, and queue for BFS from start
                    visited_from_start.add(child_state)
                    parent_from_initial[child_state] = current_state_from_initial
                    queue_from_initial.append(child_state)

                    frontier_updates.append((child_state.current_row, child_state.current_column))

                    if child_state in visited_from_goal:
                        # If the child is found in the goal's visited set, we reconstruct the path from start to goal
                        meeting_state = (child_state.current_row, child_state.current_column)
                        print(f"{step_number:<6} {'Start':<10} {str(expanded_node):<18} {str(frontier_updates):<30} {str(meeting_state):<18}")
                        path = self.construct_path(child_state, parent_from_initial, parent_from_goal)
                        print("\nBidirectional-Breadth First Search Path:", path)
                        return path

            print(f"{step_number:<6} {'Start':<10} {str(expanded_node):<18} {str(frontier_updates):<30} {str(meeting_state):<18}")

            # BFS from goal
            current_state_from_goal = queue_from_goal.popleft()
            step_number += 1

            expanded_node = (current_state_from_goal.current_row, current_state_from_goal.current_column)
            meeting_state = "-"

            frontier_updates = []

            for child_state in successors(current_state_from_goal, maze):
                if child_state not in visited_from_goal:
                    # Add the child to the visited set, parent dictionary, and queue for BFS from goal
                    visited_from_goal.add(child_state)
                    parent_from_goal[child_state] = current_state_from_goal
                    queue_from_goal.append(child_state)

                    frontier_updates.append((child_state.current_row, child_state.current_column))

                    if child_state in visited_from_start:
                        # If the child is found in the start's visited set, we reconstruct the path from start to goal
                        meeting_state = (child_state.current_row, child_state.current_column)
                        print(f"{step_number:<6} {'Goal':<10} {str(expanded_node):<18} {str(frontier_updates):<30} {str(meeting_state):<18}")
                        path = self.construct_path(child_state, parent_from_initial, parent_from_goal)
                        print("Bidirectional-Breadth First Search Path:", path)
                        return path

            print(f"{step_number:<6} {'Goal':<10} {str(expanded_node):<18} {str(frontier_updates):<30} {str(meeting_state):<18}")

        print("\nNo path found.")
        return None  # If no path is found, return none

    def construct_path(self, meeting_state, parent_from_start, parent_from_goal):
        # Reconstruct the path from start to goal through the meeting point
        # First, reconstruct the path from start to meeting point
        path_from_start = []
        current_node = meeting_state
        while current_node is not None:
            path_from_start.append((current_node.current_row, current_node.current_column))
            current_node = parent_from_start.get(current_node)
        path_from_start.reverse()  # Reverses the path from start to meeting point to get the correct order from start to meeting point

        # Secondly, reconstruct the path from meeting point to goal
        path_from_goal = []
        current_node = parent_from_goal.get(meeting_state)
        while current_node is not None:
            path_from_goal.append((current_node.current_row, current_node.current_column))
            current_node = parent_from_goal.get(current_node)

        return path_from_start + path_from_goal  # Constructs the path from start to goal through the meeting point
=======
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
>>>>>>> a613c577db7c19a3aec63dc1fceca6d342dd4b1d

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
<<<<<<< HEAD
                algorithmChoice = int(input("Enter 0 to exit or choose an algorithm choice (1-5): "))
=======
                algorithmChoice = int(input("Enter algorithm choice (1-5): "))
>>>>>>> a613c577db7c19a3aec63dc1fceca6d342dd4b1d
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if algorithmChoice == 0:
                break
            
<<<<<<< HEAD
=======
            print_maze(maze_map)
            
>>>>>>> a613c577db7c19a3aec63dc1fceca6d342dd4b1d
            if algorithmChoice == 1:
                path = bfs(maze, start_row, start_column) # WIP
                print("\nBreadth-First Search Path:", path)
                input("\nPress Enter to return to the main menu...")

            elif algorithmChoice == 2:
                path = dfs(maze, start_row, start_column) # WIP
                print("\nDepth-First Search Path:", path)
                input("\nPress Enter to return to the main menu...")

            elif algorithmChoice == 3:
<<<<<<< HEAD
                bbfs_solver = BidirectionalBFS()
                path = bbfs_solver.bidirectional_bfs(maze, start_row, start_column)
=======
                path = BidirectionalBFS.bidirectional_bfs(maze, start_row, start_column)
                print("\nBidirectional Breadth-First Search Path:", path)
>>>>>>> a613c577db7c19a3aec63dc1fceca6d342dd4b1d
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