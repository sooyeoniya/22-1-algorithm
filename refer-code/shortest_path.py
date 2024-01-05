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


class ShortestPath:
    def __init__(self, graph):
        self.graph = graph
        self.dijkstra_tree = {}
        self.bellman_ford_tree = {}
        self.floyd_warshall_p = {}

    def print_solution(self, algorithm=None):
        if algorithm == "dijkstra":
            print("*** Dijkstra Solution ***")
            for v, u in self.dijkstra_tree.items():
                print("{0} -> {1}".format(u, v))
        elif algorithm == "bellman_ford":
            print("*** Bellman Ford Solution ***")
            for v, u in self.bellman_ford_tree.items():
                print("{0} -> {1}".format(u, v))
        else:
            raise ValueError()

    def print_floyd_warshall_path(self, q, r):
        if self.floyd_warshall_p[q][r] == 0:
            print(r, end=" ")
        else:
            self.print_floyd_warshall_path(q, self.floyd_warshall_p[q][r])
            self.print_floyd_warshall_path(self.floyd_warshall_p[q][r], r)

    def dijkstra(self, start_node='1'):
        S = set()
        d = {}
        for node in self.graph.nodes:
            d[node] = sys.maxsize
        d[start_node] = 0

        while len(S) != len(self.graph.nodes):
	    # 이곳에 코딩을 추가하세요. (약 8~10라인)

    def extract_min(self, V_minus_S, d):
        min = sys.maxsize
        selected_node = None

        # 이곳에 코딩을 추가하세요. (약 5~7라인)

        return selected_node

    def bellman_ford(self, start_node='1'):
        d = {}
        for node in self.graph.nodes:
            d[node] = sys.maxsize
        d[start_node] = 0

        # 이곳에 코딩을 추가하세요. (약 5~7라인)

        return self.check_negative_cycle(d)

    def check_negative_cycle(self, d):
        is_ok = True

        # 이곳에 코딩을 추가하세요. (약 5~7라인)

        return is_ok

    def floyd_warshall(self):
        d = {}
        for node in self.graph.nodes:
            d[node] = {}
            self.floyd_warshall_p[node] = {}

        for i in self.graph.nodes:
            for j in self.graph.nodes:
                if j in self.graph.adjacency_list[i]:
                    d[i][j] = self.graph.adjacency_list[i][j]
                else:
                    d[i][j] = sys.maxsize

                self.floyd_warshall_p[i][j] = 0

        # 이곳에 코딩을 추가하세요. (약 6~8라인)


if __name__ == "__main__":
    #####################################################
    #####################################################
    ##             dijkstra algorithm test             ##
    #####################################################
    #####################################################
    dijkstra_adjacency_list = {
        '1': {'2': 8, '3': 9, '4': 11},
        '2': {'5': 10},
        '3': {'2': 6, '5': 2, '4': 3},
        '4': {'6': 9, '7': 8},
        '5': {'8': 2},
        '6': {'3': 12, '8': 5},
        '7': {'6': 7},
        '8': {'7': 4}
    }

    graph = Graph(adjacency_list=dijkstra_adjacency_list, directed=True)
    print("[Graph] number of nodes: {0}, number of edges: {1}".format(graph.num_nodes, graph.num_edges))
    print(graph.edges)
    sp = ShortestPath(graph=graph)
    sp.dijkstra(start_node='1')
    sp.print_solution(algorithm="dijkstra")

    print()

    #####################################################
    #####################################################
    ##         bellman-ford algorithm test - 1         ##
    #####################################################
    #####################################################
    bellman_ford_adjacency_list = {
        '1': {'2': 8, '3': 9, '4': 11},
        '2': {'5': 10},
        '3': {'2': -15, '5': 1, '4': 3},
        '4': {'6': 9, '7': 8},
        '5': {'8': 2},
        '6': {'3': 12, '8': 5},
        '7': {'6': -7},
        '8': {'7': 4}
    }

    graph = Graph(adjacency_list=bellman_ford_adjacency_list, directed=True)
    print("[Graph] number of nodes: {0}, number of edges: {1}".format(graph.num_nodes, graph.num_edges))
    print(graph.edges)
    sp = ShortestPath(graph=graph)
    is_ok = sp.bellman_ford(start_node='1')
    if is_ok:
        sp.print_solution(algorithm="bellman_ford")

    print()

    #####################################################
    #####################################################
    ##         bellman-ford algorithm test - 2         ##
    #####################################################
    #####################################################
    bellman_ford_adjacency_list_with_negative_cycle = {
        '1': {'2': 8, '3': 9, '4': 11},
        '2': {'5': 10},
        '3': {'2': -15, '5': 1, '4': 3},
        '4': {'6': 9, '7': 8},
        '5': {'8': 2},
        '6': {'3': -12, '8': 5},
        '7': {'6': -7},
        '8': {'7': 4}
    }

    graph = Graph(adjacency_list=bellman_ford_adjacency_list_with_negative_cycle, directed=True)
    print("[Graph] number of nodes: {0}, number of edges: {1}".format(graph.num_nodes, graph.num_edges))
    print(graph.edges)
    sp = ShortestPath(graph=graph)
    is_ok = sp.bellman_ford(start_node='1')
    if is_ok:
        sp.print_solution(algorithm="bellman_ford")

    print()

    #####################################################
    #####################################################
    ##           floyd-warshall algorithm test         ##
    #####################################################
    #####################################################
    floyd_warshall_adjacency_list = {
        '1': {'2': 1, '4': 1, '5': 5},
        '2': {'1': 9, '3': 3, '4': 2},
        '3': {'4': 4},
        '4': {'3': 2, '5': 3},
        '5': {'1': 3}
    }

    graph = Graph(adjacency_list=floyd_warshall_adjacency_list, directed=True)
    print("[Graph] number of nodes: {0}, number of edges: {1}".format(graph.num_nodes, graph.num_edges))
    print(graph.edges)
    sp = ShortestPath(graph=graph)
    is_ok = sp.floyd_warshall()

    #SOURCE: 2, DESTINATION: 1
    print('2', end=" ")
    sp.print_floyd_warshall_path(q='2', r='1')
    print()

    # SOURCE: 5, DESTINATION: 3
    print('5', end=" ")
    sp.print_floyd_warshall_path(q='5', r='3')
    print()

    # SOURCE: 2, DESTINATION: 4
    print('2', end=" ")
    sp.print_floyd_warshall_path(q='2', r='4')
    print()
