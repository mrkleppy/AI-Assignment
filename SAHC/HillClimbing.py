class Maze:
    # Initialise for the maze
    def __init__(self, mazeMap: list, end_row: int, end_column: int):
        self.mazeMap = mazeMap
        self.end_row = end_row
        self.end_column = end_column

class State:
    # Initialise for the state
    def __init__(self, current_row: int, current_column: int):
        self.current_row = current_row
        self.current_column = current_column

    # Verify the state is goal
    def is_goal(self, maze):
        return self.current_row == maze.end_row and self.current_column == maze.end_column

    # Veirfy the move is valid
    def is_valid(self, maze):     
        return (
            0 <= self.current_row < len(maze.mazeMap) and
            0 <= self.current_column < len(maze.mazeMap[0]) and
            maze.mazeMap[self.current_row][self.current_column] == 1
        )

    # Use to compare the states
    def __eq__(self, other):
        return self.current_row == other.current_row and self.current_column == other.current_column

    def __hash__(self):
        return hash((self.current_row, self.current_column))

class SAHC:
    def __init__(self, initial_maze, initial_state):
        self.maze = initial_maze
        self.current_state = initial_state
        self.path = [self.current_state]
        self.visited = set()
        self.level = 0
        self.heuristic = self.calculate_heuristic(self.current_state, self.maze)

    def SAHC(self):
        if self.current_state.is_goal(self.maze):
            return [self.current_state]

        while self.heuristic > 0:
            print("\n---------")
            print(f"LEVEL {self.level}")
            print("---------")
            print(
                f"CURRENT NODE: {self.current_state.current_row}, "
                f"{self.current_state.current_column}, {self.heuristic}"
            )

            self.visited.add(self.current_state)
            possible_moves = self.get_possible_move(self.current_state, self.maze)

            if not possible_moves:
                print("No possible moves from current state")
                break

            next_states = []
            for move in possible_moves:
                new_state = self.apply_move(self.current_state, move)
                new_heuristic = self.calculate_heuristic(new_state, self.maze)
                next_states.append((new_state, new_heuristic))

            next_states.sort(key=lambda x: x[1])
            print("OPEN LIST:", [
                (state.current_row, state.current_column, heuristic)
                for state, heuristic in next_states
            ])

            best_next_state, best_next_heuristic = next_states[0]

            if best_next_heuristic < self.heuristic and best_next_state not in self.visited:
                self.current_state = best_next_state
                self.heuristic = best_next_heuristic
                self.path.append(self.current_state)
                self.level += 1
                print("selected:", self.current_state.current_row, self.current_state.current_column, self.heuristic)
            else:
                print("there is no better move or already visited")
                print("\n ------------------------------------------------------------")
                print("Initial State:", self.path[0].current_row, self.path[0].current_column)
                print("Goal State:", self.maze.end_row, self.maze.end_column)
                print("Path:", [(state.current_row, state.current_column) for state in self.path])
                print("LOCAL MAXIMUM: There is no solution")
                return None

        print("\n ------------------------------------------------------------")
        print("Initial State:", self.path[0].current_row, self.path[0].current_column)
        print("Goal State:", self.maze.end_row, self.maze.end_column)
        print("Path:", [(state.current_row, state.current_column) for state in self.path])
        print("Solution Found!")
        return self.path

    def get_possible_move(self, current_state, maze):
        moves = []

        up_state = State(current_state.current_row - 1, current_state.current_column)
        if up_state.is_valid(maze):
            moves.append((-1, 0))

        down_state = State(current_state.current_row + 1, current_state.current_column)
        if down_state.is_valid(maze):
            moves.append((1, 0))

        left_state = State(current_state.current_row, current_state.current_column - 1)
        if left_state.is_valid(maze):
            moves.append((0, -1))

        right_state = State(current_state.current_row, current_state.current_column + 1)
        if right_state.is_valid(maze):
            moves.append((0, 1))

        return moves

    def apply_move(self, current_state, move):
        move_row, move_column = move
        return State(
            current_state.current_row + move_row,
            current_state.current_column + move_column
        )

    def calculate_heuristic(self, current_state, maze):
        return abs(current_state.current_row - maze.end_row) + abs(current_state.current_column - maze.end_column)