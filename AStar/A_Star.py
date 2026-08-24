from Maze import *
import heapq
from itertools import count

GREEN = "\033[92m"
CYAN = "\033[0;36m"
RED = "\033[31m"
RESET = "\033[0m"

def heuristic(state, maze):
    # Manhattan distance: admissible and consistent on a 4-directional unit-cost grid
    return abs(state.current_row - maze.end_row) + abs(state.current_column - maze.end_column)

def a_star(maze, start_row, start_column):
    start = State(start_row, start_column)
    goal = State(maze.end_row, maze.end_column)

    if not start.is_valid(maze) or not goal.is_valid(maze):
        print("Start or goal is invalid (wall or out of bounds).")
        return None

    counter = count()  # tie-breaker so heapq never has to compare two States directly
    g_score = {start: 0}
    open_heap = [(heuristic(start, maze), next(counter), start)]  # (f, tie, state)
    closed = set()

    step = 0
    max_frontier = 1

    while open_heap:
        f, _, current = heapq.heappop(open_heap)

        if current in closed:
            continue  # stale entry left behind by an earlier, worse relaxation of this cell

        closed.add(current)
        step += 1
        g = g_score[current]
        h = heuristic(current, maze)

        print(f"\n+----------------- Step {step}: {CYAN}A* Search{RESET} ------------------+")
        print(f"| Expanded Node       : {CYAN}({current.current_row}, {current.current_column}){RESET}   g={g} h={h} f={f}")

        if current == goal:
            print("+------------------------------------------------------------------+")

            path = []
            node = current
            while node is not None:
                path.append((node.current_row, node.current_column))
                node = node.parent
            path.reverse()

            path_str = " -> ".join(f"({r},{c})" for r, c in path)
            print(f"\nPath found! Length: {len(path)}")
            print(f"Path: {GREEN}{path_str}{RESET}")

            print(f"\n{CYAN}========================== Result =========================={RESET}")
            print(f"Completeness                            : {GREEN}Completed{RESET}")
            print("Cost (Length of Path)                   :", len(path))
            print("Time Efficiency (Nodes Expanded)        :", step)
            print("Space Efficiency (Max Nodes in Frontier):", max_frontier)
            return path

        children = successors(current, maze)  # child.parent is already set to current
        relaxed = []
        for child in children:
            tentative_g = g + 1
            if child not in g_score or tentative_g < g_score[child]:
                g_score[child] = tentative_g
                f_child = tentative_g + heuristic(child, maze)
                heapq.heappush(open_heap, (f_child, next(counter), child))
                relaxed.append((child.current_row, child.current_column, tentative_g, heuristic(child, maze), f_child))

        max_frontier = max(max_frontier, len(open_heap))

        # One row per still-live state (deduped), sorted by f, for a readable open list
        open_preview = sorted(
            (
                (s.current_row, s.current_column, sg, heuristic(s, maze), sg + heuristic(s, maze))
                for s, sg in g_score.items()
                if s not in closed
            ),
            key=lambda t: t[4]
        )

        print(f"| Possible Moves      : {[(c.current_row, c.current_column) for c in children]}")
        print(f"| Relaxed / Added     : {relaxed}")
        print(f"| Open List (f-sorted): {open_preview}")
        print(f"| Frontier Size       : {len(open_preview)}")
        print("+------------------------------------------------------------------+")

    print(f"\n{CYAN}========================== Result =========================={RESET}")
    print(f"Completeness                            : {RED}Not Complete (No solution has found){RESET}")
    print("Time Efficiency (Nodes Expanded)        :", step)
    print("Space Efficiency (Max Nodes in Frontier):", max_frontier)
    return None
