"""
    Build constructor and add_vertex method for graphs
"""

class Graph:
    def __init__(self) -> None:
        self.adj_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(f'{vertex}: {self.adj_list[vertex]}')
    
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.print_graph()