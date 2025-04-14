from collections import deque


def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    print("\nBFS Traversal Order:")
    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def create_graph():
    graph = {}
    print("Create your graph (enter 'done' when finished):")

    while True:
        node = input("\nEnter a node (or 'done' to finish): ").strip().upper()
        if not node:
            continue
        if node == 'DONE':
            break

        neighbors = input(f"Enter {node}'s neighbors (space-separated): ").upper().split()

        # Add to existing neighbors instead of overwriting
        if node not in graph:
            graph[node] = set()
        graph[node].update(neighbors)

        # Ensure bidirectional connections
        for neighbor in neighbors:
            if neighbor not in graph:
                graph[neighbor] = set()
            graph[neighbor].add(node)

    return graph


if __name__ == "__main__":
    print("🌟 Corrected BFS Implementation 🌟")
    user_graph = create_graph()

    if user_graph:
        while True:
            start_node = input("\nEnter starting node: ").strip().upper()
            if start_node in user_graph:
                break
            print("Node not in graph! Try again.")

        bfs(user_graph, start_node)
    else:
        print("No graph created. Exiting.")