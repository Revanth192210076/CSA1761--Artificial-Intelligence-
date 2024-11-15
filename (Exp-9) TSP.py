from itertools import permutations

def travelling_salesman_problem(graph, start):
    """
    Solves the Travelling Salesman Problem using brute force.

    Parameters:
    graph: A 2D list representing the adjacency matrix of the graph.
    start: The index of the starting city.

    Returns:
    The shortest path and its cost.
    """

    nodes = [i for i in range(len(graph)) if i != start]
    min_cost = float('inf')
    min_path = []

    for perm in permutations(nodes):
        path = [start] + list(perm) + [start]
        cost = 0
        for i in range(len(path) - 1):
            cost += graph[path[i]][path[i + 1]]

        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path, min_cost

if __name__ == "__main__":
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]
    start = 0
    path, cost = travelling_salesman_problem(graph, start)
    print("Shortest path:", path)
    print("Minimum cost:", cost)
