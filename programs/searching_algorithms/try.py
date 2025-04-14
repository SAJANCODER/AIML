#implementing breadth first search

from collections import deque
def bfs(graph,start):
    visited = set([start])
    queue = deque([start])

    print("BFS TRAVERSAL")
    while queue: #node accessed
        node = queue.popleft()   #pop the left value in queue
        print(node,end=" ")

        for neighbor in graph.get(node,set()):
            if neighbor not in visited :
                visited.add(neighbor)
                queue.append(neighbor)
def create_graph():
    graph={}  #initilization of graph values
    print("create your own graph!")
    while True:
        node = input("Enter the node of the graph (Done to stop):").strip().upper()
        if not node:
            continue
        if node == 'DONE':
            break
        neighbors = input(f"Enter the nighbours of {node} 's node:").upper().split()
        if node not in graph:
            graph[node]=set()
        graph[node].update(neighbors)

        for neighbor in neighbors:
            if neighbor not in graph:
                graph[neighbor]=set()
            graph[neighbor].add(node)
    return graph
if __name__ == "__main__":
    user_graph = create_graph() #creating a object for create_graph
    if user_graph:
        while True:
            start_node=input("enter the start node:").strip().upper()
            if start_node in user_graph:
                break
            print("not in graph") # this is else part
        bfs(user_graph,start_node)
    else:
        print("no graph exists")










