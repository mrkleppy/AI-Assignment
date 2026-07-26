from collections import deque
from Maze import State, successors

def bidirectional_bfs(maze, start_row, start_column):
    # Initialise the start and goal point
    start = State(start_row, start_column)
    goal = State(maze.end_row, maze.end_column)
    
    # queue for BFS from start and goal
    # deque is for efficient pop from left and append to right, for both the exit and start
    q_start = deque([start])
    q_goal = deque([goal])
    
    # visited sets for BFS from start and goal
    v_start = {start}
    v_goal = {goal}
    
    # parent dictionaries for BFS from start and goal to reconstruct the path
    p_start = {start: None}
    p_goal = {goal: None}
    
    while q_start and q_goal:
        # Since this is a bidirectional BFS, we will alternate between expanding the search from the start and the goal.
        # BFS from start
        current_start = q_start.popleft()
        for child in successors(current_start, maze):
            if child not in v_start:
                # Add the child to the visited set, parent dictionary, and queue for BFS from start
                v_start.add(child)
                p_start[child] = current_start
                q_start.append(child)
                
                if child in v_goal:
                    # If the child is found in the goal's visited set, we reconstruct the path from start to goal
                    return construct_path(child, p_start, p_goal)
    
        # BFS from goal
        current_goal = q_goal.popleft()
        for child in successors(current_goal, maze):
            if child not in v_goal:
                v_goal.add(child)
                p_goal[child] = current_goal
                q_goal.append(child)
                if child in v_start:
                    # If the child is found in the start's visited set, we reconstruct the path from start to goal
                    return construct_path(child, p_start, p_goal)
                
    return None # If no path is found, return none
                
def construct_path(meet_state, p_start, p_goal):
    # Reconstruct the path from start to goal through the meeting point
    # First, reconstruct the path from start to meeting point
    path_start = []
    node = meet_state
    while node is not None:
        path_start.append((node.current_row, node.current_column))
        node = p_start.get(node)
    path_start.reverse() # Reverses the path from start to meeting point to get the correct order from start to meeting point
    
    # Secondly, reconstruct the path from meeting point to goal
    path_goal = []
    node = p_goal.get(meet_state)
    while node is not None:
        path_goal.append((node.current_row, node.current_column))
        node = p_goal.get(node)
    
    return path_start + path_goal # Constructs the path from start to goal through the meeting point