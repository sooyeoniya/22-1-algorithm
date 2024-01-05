import sys

class Graph:
    def __init__(self, adjacency_list, directed=False):
        self.adjacency_list = adjacency_list
        self.nodes = set()
        self.edges = set()
        self.num_nodes = 0
        self.num_edges = 0

        if directed:
            for node in adjacency_list:
                for adjacency_node in adjacency_list[node]:
                    weight = adjacency_list[node][adjacency_node]
                    self._add_node_and_edge(node, adjacency_node, weight)
        else:
            for node in adjacency_list:
                for adjacency_node in adjacency_list[node]:
                    edge_exist_conditions = [
                        (node, adjacency_node, adjacency_list[node][adjacency_node]) in self.edges,
                        (adjacency_node, node, adjacency_list[adjacency_node][node]) in self.edges,
                    ]
                    if any(edge_exist_conditions):
                        assert adjacency_list[node][adjacency_node] == adjacency_list[adjacency_node][node]
                    else:
                        weight = adjacency_list[node][adjacency_node]
                        self._add_node_and_edge(node, adjacency_node, weight)

    def _add_node_and_edge(self, s, d, weight):
        if s not in self.nodes:
            self.nodes.add(s)
            self.num_nodes += 1

        if d not in self.nodes:
            self.nodes.add(d)
            self.num_nodes += 1

        self.edges.add((s, d, weight))
        self.num_edges += 1


class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        self.rank = {}

    def make_set(self):
        for v in self.vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find_set(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find_set(self.parent[item])

        return self.parent[item]

    def union(self, x, y):
        xroot = self.find_set(x)
        yroot = self.find_set(y)

        # 이곳에 코딩을 추가하세요. (약 5~7라인)


class SpanningTree:
    def __init__(self, graph):
        self.graph = graph
        self.prim_tree = {}
        self.kruskal_tree = []

    def print_solution(self, algorithm=None):
        if algorithm == "prim":
            print("*** Prim Solution ***")
            for v, u in self.prim_tree.items():
                print("{0} - {1}".format(u, v))
        elif algorithm == "kruskal":
            print("*** Kruskal Solution ***")
            for u, v in self.kruskal_tree:
                print("{0} - {1}".format(u, v))
        else:
            raise ValueError()

    def prim(self, start_node='1'):
        S = set()
        d = {}
        for node in self.graph.nodes:
            d[node] = sys.maxsize
        d[start_node] = 0

        while len(S) != len(self.graph.nodes):
            V_minus_S = self.graph.nodes - S
            
	    # 이곳에 코딩을 추가하세요. (약 8~10라인)

    def extract_min(self, V_minus_S, d):
        min = sys.maxsize
        selected_node = None

        # 이곳에 코딩을 추가하세요. (약 5~7라인)

        return selected_node

    def kruskal(self):
        ds = DisjointSet(self.graph.nodes)
        ds.make_set()

        i = 0
        e = 0
        sorted_edges = sorted(self.graph.edges, key=lambda edge: edge[2])

        while e < self.graph.num_nodes - 1:
	    # 이곳에 코딩을 추가하세요. (약 9~11라인)


if __name__ == "__main__":
    adjacency_list = {
        '1': {'2': 8, '3': 9, '4': 11},
        '2': {'1': 8, '5': 14},
        '3': {'1': 9, '4': 13, '5': 5, '6': 12},
        '4': {'1': 11, '3': 13, '6': 9, '7': 8},
        '5': {'2': 14, '3': 5},
        '6': {'3': 12, '4': 9, '7': 7},
        '7': {'4': 8, '6': 7}
    }

    graph = Graph(adjacency_list=adjacency_list)
    print("[Graph] number of nodes: {0}, number of edges: {1}".format(graph.num_nodes, graph.num_edges))
    print(graph.edges)
    st = SpanningTree(graph=graph)
    st.prim(start_node='1')
    st.print_solution(algorithm="prim")

    st.kruskal()
    st.print_solution(algorithm="kruskal")