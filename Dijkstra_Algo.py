import heapq

def dijkstra(graph, start):
    dist = {node: float('infinity') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist > dist[curr_node]:
            continue

        for neighbor, weight in graph[curr_node].items():
            distance = curr_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist

#Example from the book
graph = {
    'S': {'T': 10, 'Y': 5, 'Z':7},
    'T': {'X':1, 'Y':2},
    'X': {'Z': 4},
    'Y': {'Z': 2, 'T': 3, 'X': 9},
    'Z': {'S': 7, 'X': 6}
}

start_node = 'S'
dist = dijkstra(graph, start_node)

for node, distance in dist.items():
    print(f"Shortest path from {start_node} to {node} is {distance}")

'''Output:
Shortest path from S to S is 0
Shortest path from S to T is 8
Shortest path from S to X is 9
Shortest path from S to Y is 5
Shortest path from S to Z is 7 '''
