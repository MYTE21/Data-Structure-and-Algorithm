visited = []
queue = []
ans = []

def bfs(graph, node, visited):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        ans.append(s)
        for neighbour in graph[s]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

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

    ans = bfs(graph, start_node, visited)
    print("Visited Node : ",ans, "\n")


