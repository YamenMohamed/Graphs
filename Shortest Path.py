from queue import PriorityQueue

graph = {
    'S': [('T', 10), ('Y', 5)],
    'X': [('Z', 4)],
    'Y': [('T', 3), ('Z', 2), ('X', 9)],
    'Z': [('X', 4), ('S', 7)],
    'T': [('Y', 2), ('X', 1)],
}


class Node:
    def __init__(self, vertex, distance):
        self.v = vertex
        self.distance = distance

    def __lt__ (self,other):                    #comparator
        return self.distance < other.distance


def dijkstra(graph, s):
    visited = set()
    P = PriorityQueue()
    P.put(Node(s, 0))
    shortestPaths = {}
    shortestPaths[s] = Node(s,0)

    while not P.empty():
        node = P.get()
        vertex = node.v
        distance = node.distance
        visited.add(vertex)
        for v1,d1 in graph[vertex]:  # edge[0] = vertex  //  edge[1] = weight
            if v1 not in visited:
                if v1 not in shortestPaths:
                    shortestPaths[v1] = Node(vertex, distance + d1)
                else:
                    newNode = shortestPaths[v1]
                    if distance + d1 < newNode.distance:
                        newNode.distance = distance + d1

                P.put(Node(v1, distance + d1))

    for node in shortestPaths:
        print(node,shortestPaths[node].distance)



source = 'S'
dijkstra(graph, source)

