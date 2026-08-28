from Maze import *
import heapq
from itertools import count

GREEN = "\033[92m"
CYAN = "\033[0;36m"
RED = "\033[31m"
RESET = "\033[0m"

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
            print(f"| {'Expanded Node':<20}: {CYAN}({current.current_row}, {current.current_column}){RESET}   g={g} h={h} f={f}")

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
        possible_moves = []
        relaxed = []
        for child in children:
            # The cost to reach a neighbour is always one more step than the current state
            tentative_g = g + 1
            h_child = self.heuristic(child)
            f_child = tentative_g + h_child
            move_str = f"({child.current_row}, {child.current_column}) g={tentative_g} h={h_child} f={f_child}"
            possible_moves.append(move_str)

            # Only keep this neighbour if it is new, or the path found to it is better than before
            if child not in self.g_score or tentative_g < self.g_score[child]:
                self.g_score[child] = tentative_g
                heapq.heappush(self.open_heap, (f_child, next(self.counter), child))
                relaxed.append(move_str)

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
        open_preview_labeled = [f"({r}, {c}) g={sg} h={h} f={f}" for r, c, sg, h, f in open_preview]

        print(f"| {'Possible Moves':<20}: [{', '.join(possible_moves)}]")
        print(f"| {'Relaxed / Added':<20}: [{', '.join(relaxed)}]")
        print(f"| {'Open List (f-sorted)':<20}: [{', '.join(open_preview_labeled)}]")
        print(f"| {'Frontier Size':<20}: {len(open_preview)}")
        if open_preview:
            nr, nc, ng, nh, nf = open_preview[0]
            print(f"| {'Selected Next':<20}: ({nr}, {nc})  g={ng} h={nh} f={nf}   <- lowest f")
        else:
            print(f"| {'Selected Next':<20}: None (frontier empty)")
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
