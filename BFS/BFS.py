from Maze import *

GREEN = "\033[92m"
RESET = "\033[0m"

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