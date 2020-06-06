visited = []
ans = []

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        ans.append(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

    return ans

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    start_node = 'A'
    ans = dfs(graph, start_node, visited)
    print("DFS : ", ans, "\n")

