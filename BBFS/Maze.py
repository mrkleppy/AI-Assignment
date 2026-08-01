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