from collections import deque

def bfs(graph, start):

    visited = set()  
    queue = deque([start])  
    visited.add(start)  

    result = []

    while queue:
        current_node = queue.popleft() 
        result.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS traversal:", bfs(graph, 'A')) 
