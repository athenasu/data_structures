"""
    Build remove_edge method for graphs
"""

class Graph:
    def __init__(self) -> None:
        self.adj_list = {}
    
    def add_vertex(self, vertex) -> bool:
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2) -> bool:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2) -> bool:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def print_graph(self) -> None:
        for vertex in self.adj_list:
            print(f'{vertex}: {self.adj_list[vertex]}')
    
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')

my_graph.print_graph()

my_graph.remove_edge('A', 'B')

my_graph.print_graph()

# trying to remove an edge that doesn't exist
my_graph.remove_edge('A', 'D')