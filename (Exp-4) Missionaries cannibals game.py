from collections import deque

def is_valid(state):
    """Check if a state is valid (no missionaries eaten)."""
    m_left, c_left, m_right, c_right = state
    # Check if missionaries are safe on both sides
    if (m_left >= c_left or m_left == 0) and (m_right >= c_right or m_right == 0):
        return True
    return False

def get_possible_moves(state, boat_on_left):
    """Generate possible moves from the current state."""
    m_left, c_left, m_right, c_right = state
    moves = []
    
    # Possible moves depending on boat position
    if boat_on_left:
        if m_left >= 2:
            moves.append((m_left - 2, c_left, m_right + 2, c_right))
        if m_left >= 1:
            moves.append((m_left - 1, c_left, m_right + 1, c_right))
        if c_left >= 2:
            moves.append((m_left, c_left - 2, m_right, c_right + 2))
        if c_left >= 1:
            moves.append((m_left, c_left - 1, m_right, c_right + 1))
        if m_left >= 1 and c_left >= 1:
            moves.append((m_left - 1, c_left - 1, m_right + 1, c_right + 1))
    else:
        if m_right >= 2:
            moves.append((m_left + 2, c_left, m_right - 2, c_right))
        if m_right >= 1:
            moves.append((m_left + 1, c_left, m_right - 1, c_right))
        if c_right >= 2:
            moves.append((m_left, c_left + 2, m_right, c_right - 2))
        if c_right >= 1:
            moves.append((m_left, c_left + 1, m_right, c_right - 1))
        if m_right >= 1 and c_right >= 1:
            moves.append((m_left + 1, c_left + 1, m_right - 1, c_right - 1))
            
    # Filter valid moves
    return [move for move in moves if is_valid(move)]

def solve_missionaries_and_cannibals():
    """Solve the Missionaries and Cannibals problem using BFS."""
    initial_state = (3, 3, 0, 0)  # (missionaries_left, cannibals_left, missionaries_right, cannibals_right)
    goal_state = (0, 0, 3, 3)
    boat_on_left = True  # Initially, the boat is on the left side
    queue = deque([(initial_state, boat_on_left, [])])
    visited = set([(initial_state, boat_on_left)])

    while queue:
        current_state, boat_on_left, path = queue.popleft()

        # Check if we reached the goal state
        if current_state == goal_state:
            return path + [current_state]

        # Generate next states (possible moves)
        next_states = get_possible_moves(current_state, boat_on_left)
        
        for next_state in next_states:
            # Toggle boat side
            next_boat_on_left = not boat_on_left
            if (next_state, next_boat_on_left) not in visited:
                visited.add((next_state, next_boat_on_left))
                queue.append((next_state, next_boat_on_left, path + [current_state]))

    return "No solution found"

# Run the solver
solution = solve_missionaries_and_cannibals()
if solution != "No solution found":
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print(solution)
