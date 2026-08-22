from Maze import *
from Maze_generator import generate_maze


class DepthFirstSearch():
    maxFrontier = 0
    numOfIteration = 0

    def dfs(self, maze, start_row, start_column):
        start = State(start_row, start_column)
        if start.is_goal(maze): return start

        frontier = [start] # DFS stack
        visited = {start} # stores non duplicate values. here, stores visited and rejecting duplicates
        #parent = {start: None} # {child: parent}

        while frontier: # proceed if stack has nodes
            self.numOfIteration += 1

            current = frontier.pop(0) # get first element

            if current.is_goal(maze):
                return current

            visited.add(current)

            for child in successors(current, maze): # add tracing
                if child not in visited and child not in frontier:
                    frontier.insert(0, child)

                    if len(frontier) > self.maxFrontier: self.maxFrontier = len(frontier)
        
    def construct_path(self, current):
        path = [current]
        self.parent = current.parent

        while self.parent:
            path.insert(0, self.parent)
            self.parent = self.parent.parent

        return path

    def result(self, path):
        print("Time Efficiency (Nodes Expanded): ", self.numOfIteration)
        print("Space Efficiency (Max Nodes in Frontier): ", self.maxFrontier)
        
def main():
    rows, columns = 7,7

    maze_map = generate_maze(rows, columns)
    maze = Maze(maze_map, rows-1, columns-1)
    Dfs = DepthFirstSearch()

    solution = Dfs.dfs(maze, 0, 0)

    path = Dfs.construct_path(solution)
    print("Maze:\n")

    for row in maze_map:
        print(row)

    print("Path: ", end="")

    for node in path:
        if node is not None:
            print(f"({node.current_row}, {node.current_column})", end=", ")

    print("\n")
    Dfs.result(path)
    
if __name__ == "__main__":
    main()
