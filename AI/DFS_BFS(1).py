from collections import defaultdict, deque

# Create an empty adjacency list
graph = defaultdict(list)

# Input number of nodes and edges
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

# Input edges
print("Enter edges (e.g. A B means edge between A and B):")
for _ in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)  # Because it's an undirected graph

# Recursive DFS
def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    print(vertex, end=' ')
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# BFS using queue
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Input start node for traversal
start_node = input("Enter start node for traversal: ")

# Perform DFS and BFS
print("\nDFS Traversal:")
dfs(graph, start_node)

print("\nBFS Traversal:")
bfs(graph, start_node)
