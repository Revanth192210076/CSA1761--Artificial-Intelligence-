from collections import deque

def water_jug_problem(jug_a_capacity, jug_b_capacity, target_amount):
    
    visited = set()
    queue = deque([(0, 0)])  # Initial state: both jugs are empty

    while queue:
        current_a, current_b = queue.popleft()
        if current_a == target_amount or current_b == target_amount:
            return [(current_a, current_b)]  # Solution found

        # Generate possible next states
        for next_state in [
            (jug_a_capacity, current_b),  # Fill Jug A
            (current_a, jug_b_capacity),  # Fill Jug B
            (0, current_b),  # Empty Jug A
            (current_a, 0),  # Empty Jug B
            (current_a - (jug_b_capacity - current_b), jug_b_capacity) if current_a > jug_b_capacity - current_b else (0, current_a + current_b),  # Pour from A to B
            (jug_a_capacity - (current_a - current_b), 0) if current_b > current_a else (current_a + current_b, 0)  # Pour from B to A
        ]:
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

    return None  # No solution found

# Example usage
jug_a_cap = 4
jug_b_cap = 3
target = 2

solution = water_jug_problem(jug_a_cap, jug_b_cap, target)

if solution:
    print("Solution path:", solution)
else:
    print("No solution exists.")
