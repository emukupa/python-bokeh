import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()
# print(graph_data.vertexes)

N = len(graph_data.vertexes)
node_indices = list(range(N))
# print(node_indices)

start = []
end = []

color_list = []
for i, vertex in enumerate(graph_data.vertexes):
    color_list.append(vertex.color)
    if(len(vertex.edges)):
        for edge in vertex.edges:
            j = graph_data.vertexes.index(edge.destination)
            start.append(i)
            end.append(j)

print(start, end)

plot = figure(title='Graph Layout Demonstration', x_range=(
    0, 500), y_range=(0, 500), tools='', toolbar_location=None)
#plot = figure(title='Graph Layout Demonstration', x_range=(-1.1, 1.1), y_range=(-1.1, 1.1), tools='', toolbar_location=None)
graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(Spectral8, 'color')
graph.node_renderer.glyph = Oval(height=25, width=25, fill_color='color')

#graph.edge_renderer.data_source.data = dict(start=[0]*N, end=node_indices)
graph.edge_renderer.data_source.data = dict(start=start, end=end)
# start of layout code

'''
circ = [i*2*math.pi/8 for i in node_indices]
x = [math.cos(i) for i in circ]
y = [math.sin(i) for i in circ]
'''

x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)
