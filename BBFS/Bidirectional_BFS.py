from collections import deque
from Maze import State, successors

def bidirectional_bfs(maze, start_row, start_column):
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
                    path = construct_path(child_state, parent_from_initial, parent_from_goal)
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
                    path = construct_path(child_state, parent_from_initial, parent_from_goal)
                    print("Bidirectional-Breadth First Search Path:", path)
                    return path

        print(f"{step_number:<6} {'Goal':<10} {str(expanded_node):<18} {str(frontier_updates):<30} {str(meeting_state):<18}")

    print("\nNo path found.")
    return None  # If no path is found, return none

def construct_path(meeting_state, parent_from_start, parent_from_goal):
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