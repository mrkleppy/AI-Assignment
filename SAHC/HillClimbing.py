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