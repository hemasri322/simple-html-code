class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_node)
        print(start_node)

        for neighbor in self.adjacency_list[start_node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

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

print("DFS Traversal:")
graph.dfs('A')
