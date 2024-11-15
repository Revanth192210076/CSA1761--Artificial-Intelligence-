import heapq

def a_star(graph, start, goal, h):
    """
    A* algorithm implementation to find the shortest path.
    
    :param graph: A dictionary representing the graph. Each node has a list of tuples representing (neighbor, cost).
    :param start: The starting node.
    :param goal: The goal node.
    :param h: A dictionary with heuristic values for each node.
    :return: The shortest path and its cost.
    """
    # Priority queue to select the node with the lowest f(n) value
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # Maps to store the cost to reach each node and the path taken
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    came_from = {}
    
    # While there are nodes to explore
    while open_set:
        # Pop the node with the lowest f(n) value
        current_f, current = heapq.heappop(open_set)
        
        # If we reached the goal, reconstruct and return the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[goal]
        
        # Explore neighbors of the current node
        for neighbor, cost in graph[current]:
            # Calculate the tentative g(n) score
            tentative_g_score = g_score[current] + cost
            
            # Only proceed if we find a better path to neighbor
            if tentative_g_score < g_score[neighbor]:
                # Update the path and scores
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + h[neighbor]
                heapq.heappush(open_set, (f_score, neighbor))
    
    # If the goal was not reached
    return None, float('inf')

# Example usage

# Graph representation where each node has a list of tuples (neighbor, cost)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 1), ('E', 3)],
    'C': [('A', 3), ('F', 2)],
    'D': [('B', 1), ('G', 2)],
    'E': [('B', 3), ('G', 1)],
    'F': [('C', 2), ('G', 2)],
    'G': [('D', 2), ('E', 1), ('F', 2)]
}

# Heuristic values for each node (e.g., straight-line distance to the goal)
heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

# Find shortest path from 'A' to 'G'
path, cost = a_star(graph, 'A', 'G', heuristic)
print("Shortest path:", path)
print("Path cost:", cost)
