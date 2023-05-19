from queue import PriorityQueue
def prim(graph, s):
    P = PriorityQueue()
    P.put((0, None, s)) #(priority: D(s) =0 ,parent,node to begin with)
    visited = set() # to avoid cycles -> to not repeat nodes
    MinSpanningTree = []

    while not P.empty():
        weight, parent, vertex = P.get() # .get function returns the edge with lowest priority

        if vertex in visited: #if visited means min weight of node x is already inserted, then rest of weights are larger so skip it
            continue
        visited.add(vertex) # insert visited node to the set to avoid repetition

        if weight > 0 and parent is not None: # not root 3ashan adakhal edge
            MinSpanningTree.append((parent, vertex, weight)) # add lowest edge to mst

#all edges will be inserted in pq
        for neighbor, neighbor_weight in graph[vertex]: # returns list of edges and weights connected to node
            if neighbor not in visited : # add all neighbors to P with their new weights
                P.put((neighbor_weight, vertex, neighbor))

    return MinSpanningTree


def weight(array):
    totalWeight = 0
    for _, _, weight in array:
        totalWeight = totalWeight + weight
    return totalWeight


graph = {
    'S': [('T', 10), ('Y', 5)],
    'X': [('Z', 4)],
    'Y': [('T', 3), ('Z', 2), ('X', 9)],
    'Z': [('X', 4), ('S', 7)],
    'T': [('Y', 2), ('X', 1)],

}
# single source is A
mst = prim(graph, 'S')
for edge in mst:
    print(edge)
print(f"weight of Minimum Spanning tree is :{weight(mst)}")
