import random

class Edge:
    def __init__(self, destination):
        self.destination = destination


class Vertex:
    def __init__(self, value, **pos):  # TODO: test default arguments
        self.value = value
        self.color = 'white'
        self.pos = pos
        self.edges = []


class Graph:
    def __init__(self):
        self.vertexes = []

    #Create a random graph
    def randomize(width, height, pxBox, probability = 0.6):
        # Helper function to set up two-way edges
        def connectVerts(v0, v1):
            v0.edges.push(new Edge(v1))
            v1.edges.push(new Edge(v0))


            count = 0

            # Build a grid of verts
            let grid = [];
            for (let y = 0; y < height; y++) {
            let row = [];
            for (let x = 0; x < width; x++) {
                let v = new Vertex();
                //v.value = 'v' + x + ',' + y;
                v.value = 'v' + count++;
                row.push(v);
            }
            grid.push(row);
            }

            // Go through the grid randomly hooking up edges
            for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                // Connect down
                if (y < height - 1) {
                if (Math.random() < probability) {
                    connectVerts(grid[y][x], grid[y + 1][x]);
                }
                }

                // Connect right
                if (x < width - 1) {
                if (Math.random() < probability) {
                    connectVerts(grid[y][x], grid[y][x + 1]);
                }
                }
            }
            }

            // Last pass, set the x and y coordinates for drawing
            const boxBuffer = 0.8;
            const boxInner = pxBox * boxBuffer;
            const boxInnerOffset = (pxBox - boxInner) / 2;

            for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                grid[y][x].pos = {
                x: (x * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
                y: (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
                };
            }
            }

            // Finally, add everything in our grid to the vertexes in this Graph
            for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                this.vertexes.push(grid[y][x]);
            }
            }
        }

        /**
        * Dump graph data to the console
        */
        dump() {
            let s;

            for (let v of this.vertexes) {
            if (v.pos) {
                s = v.value + ' (' + v.pos.x + ',' + v.pos.y + '):';
            } else {
                s = v.value + ':';
            }

            for (let e of v.edges) {
                s += ` ${e.destination.value}`;
            }
            console.log(s);
            }
        }

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

        # start=[0, 2, 3], end=[1,1, 4]
        self.vertexes.extend(
            [debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4, debug_vertex_5, debug_vertex_6])

    def bfs(self, start):
        random_color = '#' + \
            ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        queue = []
        found = []
        queue.append(start)
        found.append(start)

        start.color = random_color

        while (len(queue) > 0):
            v = queue[0]
            for edge in v.edges:
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color

            queue.pop(0)  # TODo look at collections.dequeue
        return found

    # Get the connected components
    getConnectedComponents():
        # Connected Components
        # Go to the next unfound vertex in graph vertexes and call BFS on it
        # Go to step 1 until we get to the end of the array(loop)

        searched = []

        for vertex in self.vertexes:
            if vertex not in searched:
                searched.append(self.bfs(vertex))
