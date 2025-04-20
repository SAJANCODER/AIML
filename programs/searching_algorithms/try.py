from collections import deque #deque stands for double ended adding nodes
def bfs(graph,start):
    visited= set([start])
    queue = deque([start])
    print("BFS TRAVERSAL")
    #since i need to visit the queue , so i need a looping statement to visit until the end
    while queue:
        #i have started with a node , so i need to pop the node which i have started with
        node = queue.popleft()
        print(node,end=" ") #print the current node
        for neighbor in graph.get(node,set()):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
def creat_graph():
    graph={} #initilize the graph, as per the user.
    while True:
        node = input("enter the node : (DONE) to exit:").strip().upper()
        if not node:
            continue
        if node == 'DONE':
            break
        neighbors=input(f"enter the {node} neighbor:").upper().split()
        if node not in graph:
            graph[node]=set()
        graph[node].update(neighbors)

        for neighbor in neighbors:
            if neighbor not in graph:
                graph[neighbor]=set()
                graph[neighbor].add(node)
    return graph
if __name__=="__main__":
    user_graph = creat_graph()
    if user_graph:
        while True:
            start_node = input("Enter the start node:").upper().strip()
            if start_node in user_graph:
                break
            print("user node not in graph")
        bfs(user_graph,start_node)
    else:
        print("no graph exitst")







