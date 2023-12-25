import networkx as nx

with open('input', 'r') as fp:
    data = fp.read()

data = data.split("\n")

connections = nx.Graph()

for row in data:
    source, destinations = row.split(": ")
    destinations = destinations.split(" ")
    for destination in destinations:
        connections.add_edge(source, destination)

cuts = nx.minimum_edge_cut(connections)
connections.remove_edges_from(cuts)
groups = nx.connected_components(connections)

lengths = 1
for group in groups:
    lengths *= len(group)

print("Sum 1", lengths)
