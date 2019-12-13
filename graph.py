class GraphNode():
    def __init__(self, item):
        self.item = item
        self.neighbors = dict()
    
    def __hash__(self):
        return hash(self.item)
    
    def add_neighbor(self, neighbor_node):
        if neighbor_node in self.neighbors:
            self.neighbors[neighbor_node] += 1
        else:
            self.neighbors[neighbor_node] = 1
    
    def network(self):
        seen = {self}
        queue = [self]
        while len(queue) > 0:
            # remove (dequeue) the first item of the queue
            current_vert = queue.pop(0)
            # for all the neighbors of the removed vertex
            for neighbor in current_vert.neighbors:
                # make sure we haven't seen the vertex yet
                if neighbor not in seen:
                    # add the neighbor to seen
                    seen.add(neighbor)
                queue.append(neighbor)
        return seen


class Graph():
    def __init__(self, edge_list=None):
        self.graph = dict()
        self.size = 0
        if edge_list:
            self.add_edges(edge_list)
    
    def _get_node(self, item):
        if item not in self.graph:
            self.graph[item] = GraphNode(item)
        return self.graph[item]

    def add_edges(self, edge_list):
        for edge_1, edge_2 in edge_list:
            self.add_edge(edge_1, edge_2)
            self.add_edge(edge_2, edge_1)
    
    def add_edge(self, edge_1, edge_2):
        edge_node_1 = self._get_node(edge_1)
        edge_node_2 = self._get_node(edge_2)
        edge_node_1.add_neighbor(edge_node_2)
        edge_node_2.add_neighbor(edge_node_1)