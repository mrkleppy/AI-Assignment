from Maze import *
from Maze_generator import generate_maze


class DepthFirstSearch():
    maxFrontier = 0
    numOfIteration = 0
    completed = False

    def dfs(self, maze, start_row, start_column):
        start = State(start_row, start_column)
        if start.is_goal(maze): return start

        frontier = [start] # DFS stack
        visited = {start} # stores non duplicate values. here, stores visited and rejecting duplicates

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
        
    def trace(self, start, maze, current, frontier, visited, children, completed):
        print(f"============= Step {self.numOfIteration} =============")
        print(f"Initial State: ({start.current_row}, {start.current_column})")
        print(f"Goal State   : ({maze.end_row}, {maze.end_column})")
        if completed: print(" -  Reached")
        print(f"Current State: ({current.current_row}, {current.current_column})")
        print(f"Successors   : ", end = "")
        print(", ".join(f"({node.current_row}, {node.current_column})" for node in children), end="")
        print(f"\nFrontier     : ", end = "")
        print(", ".join(f"({node.current_row}, {node.current_column})" for node in frontier), end="")
        print(f"\nVisited      : ", end = "")
        print(", ".join(f"({node.current_row}, {node.current_column})" for node in visited), end="")
        print("\n")

    def construct_path(self, current):
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
        else: print("Not Complete (No solution has found)")
        print("Cost (Length of Path)                   :", len(path)) 
        print("Time Efficiency (Nodes Expanded)        :", self.numOfIteration)
        print("Space Efficiency (Max Nodes in Frontier):", self.maxFrontier)
        
def main():
    rows, columns = 10, 10

    maze_map = generate_maze(rows, columns)
    maze = Maze(maze_map, rows-1, columns-1)
    Dfs = DepthFirstSearch()

    solution = Dfs.dfs(maze, 0, 0)

    path = Dfs.construct_path(solution)
    print("================== Maze ==================")

    for row in maze_map:
        print(row)

    print("\nPath: ", end="")
    print(", ".join(f"({node.current_row}, {node.current_column})" for node in path if node is not None))
    print("")

    Dfs.result(path)
    
if __name__ == "__main__":
    main()
