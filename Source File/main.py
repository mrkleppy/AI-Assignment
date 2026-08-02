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
                path = bfs(maze, start_row, start_column) # WIP
                print("\nBreadth-First Search Path:", path)
                input("\nPress Enter to return to the main menu...")

            elif algorithmChoice == 2:
                path = dfs(maze, start_row, start_column) # WIP
                print("\nDepth-First Search Path:", path)
                input("\nPress Enter to return to the main menu...")

            elif algorithmChoice == 3:
                bbfs_solver = BidirectionalBFS()
                path = bbfs_solver.bidirectional_bfs(maze, start_row, start_column)
                input("\nPress Enter to return to the main menu...")

            elif algorithmChoice == 4:
                path = a_star(maze, start_row, start_column) # WIP
                print("\nA* Path:", path)
                input("\nPress Enter to return to the main menu...")

            elif algorithmChoice == 5:
                initial_state = State(start_row, start_column)
                sahc = SAHC(maze, initial_state)
                path = sahc.SAHC()

                if path is not None:
                    print("\nSteepest-Ascent Hill Climbing Path:", [(s.current_row, s.current_column) for s in path])
                else:
                    print("\nSteepest-Ascent Hill Climbing Path: No solution")
                input("\nPress Enter to return to the main menu...")
                
            else:
                print("Invalid algorithm choice.")
        
if __name__ == "__main__":
    main()