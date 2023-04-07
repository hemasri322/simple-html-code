import heapq

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def dijkstra(self, start):
        # Create a dictionary to store the distance to each vertex
        distances = {vertex: float('infinity') for vertex in self.adjacency_list}
        distances[start] = 0

        # Create a priority queue to store vertices by their minimum distance
        pq = [(0, start)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            # Skip this iteration if we have already found a shorter path to the current vertex
            if current_distance > distances[current_vertex]:
                continue

            # Update the distances to each neighbor of the current vertex
            for neighbor, weight in self.adjacency_list[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

# Example usage:
adjacency_list = {
    'A': {'B': 3, 'D': 1},
    'B': {'A': 3, 'D': 3, 'C': 1},
    'C': {'B': 1, 'D': 1, 'E': 5},
    'D': {'A': 1, 'B': 3, 'C': 1, 'E': 2},
    'E': {'D': 2, 'C': 5}
}

graph = Graph(adjacency_list)

print("Shortest distances from A:")
print(graph.dijkstra('A'))
