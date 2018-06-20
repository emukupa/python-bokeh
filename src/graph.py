class Edge:
    def __init__(self, destination):
        self.destination = destination


class Vertex:
    def __init__(self, value="default", **pos):  # TODO: test default arguments
        self.value = value
        self.color = '#ccc'
        self.pos = pos
        self.edges = []


class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('t1', x=40, y=40)
        debug_vertex_2 = Vertex('t2', x=60, y=140)
        debug_vertex_3 = Vertex('t3', x=400, y=340)
        debug_vertex_4 = Vertex('t4', x=200, y=90)
        debug_vertex_5 = Vertex('t5', x=100, y=240)
        debug_vertex_6 = Vertex('t6', x=300, y=40)

        debug_edge_1 = Edge(debug_vertex_2)  # 1 -> 2,  index 0 -> index 1
        debug_vertex_1.edges.append(debug_edge_1)

        debug_edge_2 = Edge(debug_vertex_2)
        # 3 -> 2, index 2 ->  index 1
        debug_vertex_3.edges.append(debug_edge_2)

        debug_edge_5 = Edge(debug_vertex_5)  # 4 -> 5 index 3 -> index 4
        debug_vertex_4.edges.append(debug_edge_5)

        # start=[0, 2, 4], end=[1,1, 5]
        self.vertexes.extend(
            [debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4, debug_vertex_5, debug_vertex_6])
