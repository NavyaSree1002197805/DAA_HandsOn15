def bellman_ford(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    for u in graph:
        for v, weight in graph[u].items():
            if dist[u] + weight < dist[v]:
                print("Graph contains negative weight cycle")
                return {}

    return dist

#Example from the book
graph_bellamFord = {
    'S': {'T': 6, 'Y': 7},
    'T': {'X': 5, 'Y': 8, 'Z': -4},
    'X': {'T':-2},
    'Y': {'X': -3, 'Z': 9},
    'Z': {'S': 2, 'X':7}
}

start_node_bf = 'S'
dist_bf = bellman_ford(graph_bellamFord, start_node_bf)

for node, distance in dist_bf.items():
    print(f"Shortest path from {start_node_bf} to {node} is {distance}")

'''Output:
Shortest path from S to S is 0
Shortest path from S to T is 2
Shortest path from S to X is 4
Shortest path from S to Y is 7
Shortest path from S to Z is -2 '''
