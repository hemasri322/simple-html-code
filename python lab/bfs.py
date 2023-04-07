from collections import deque

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                print(node)

                for neighbor in self.adjacency_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

# Example usage:
adjacency_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

graph = Graph(adjacency_list)

print("BFS Traversal:")
graph.bfs('A')
