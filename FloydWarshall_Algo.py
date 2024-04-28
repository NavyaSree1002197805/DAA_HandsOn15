def floyd_warshall(graph):

    dist = {node1: {node2: float('inf') for node2 in graph} for node1 in graph}
    for node1 in graph:
        dist[node1][node1] = 0
        for node2, weight in graph[node1].items():
            dist[node1][node2] = weight

    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example from the book
graph_floydWarshall= {
    '1': {'2': 3, '3':8, '5':-4},
    '2': {'5': 7, '4':1},
    '3': {'2':4},
    '4': {'3':-5, '1':2},
    '5': {'4':6}
}

distances = floyd_warshall(graph_floydWarshall)
for node1 in graph:
    for node2 in graph:
        print(f"Distance from {node1} to {node2}: {distances[node1][node2]}")

'''Output:
Distance from 1 to 1: 0
Distance from 1 to 2: 1
Distance from 1 to 3: -3
Distance from 1 to 4: 2
Distance from 1 to 5: -4
Distance from 2 to 1: 3
Distance from 2 to 2: 0
Distance from 2 to 3: -4
Distance from 2 to 4: 1
Distance from 2 to 5: -1
Distance from 3 to 1: 7
Distance from 3 to 2: 4
Distance from 3 to 3: 0
Distance from 3 to 4: 5
Distance from 3 to 5: 3
Distance from 4 to 1: 2
Distance from 4 to 2: -1
Distance from 4 to 3: -5
Distance from 4 to 4: 0
Distance from 4 to 5: -2
Distance from 5 to 1: 8
Distance from 5 to 2: 5
Distance from 5 to 3: 1
Distance from 5 to 4: 6
Distance from 5 to 5: 0 '''
