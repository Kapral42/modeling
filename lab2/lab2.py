#!/usr/bin/python

import sys
import random
from graphviz import Graph

def gen_graph_deep(n_node, max_deep):
    nodes = range(n_node)
    used_nodes = []
    edges = []
    deeps = {}

    root = random.randint(0, n_node - 1)
    used_nodes.append(root)
    nodes.remove(root)
    deeps[root] = 0
    while len(nodes) > 0:
        x = used_nodes[random.randint(0, len(used_nodes) - 1)]
        y = nodes[random.randint(0, len(nodes) - 1)]

        if deeps[x] + 1 > max_deep:
            continue

        used_nodes.append(y)
        nodes.remove(y)
        deeps[y] = deeps[x] + 1
        edges.append(str(x) + '-' + str(y))

    return edges

def gen_graph_degree(n_node, max_degree):
    nodes = range(n_node)
    used_nodes = []
    edges = []
    degrees = {}

    root = random.randint(0, n_node - 1)
    used_nodes.append(root)
    nodes.remove(root)
    degrees[root] = 0
    while len(nodes) > 0:
        x = used_nodes[random.randint(0, len(used_nodes) - 1)]
        y = nodes[random.randint(0, len(nodes) - 1)]

        if degrees[x] + 1 > max_degree:
            continue

        used_nodes.append(y)
        nodes.remove(y)
        degrees[y] = 1
        degrees[x] += 1
        edges.append(str(x) + '-' + str(y))

    return edges

def graph_draw(nodes, edges, name):
    colors = ['coral', 'lightblue2', 'lightgrey', 'aquamarine1', \
              'gold', 'deeppink1', 'deeppink1', 'orange']

    g = Graph(name, format = "png")
    for node in nodes:
        color = colors[random.randint(0, len(colors) - 1)]
        g.node(str(node), color=color, style='filled')
    for edge in edges:
        x = edge.split('-')[0]
        y = edge.split('-')[1]
        g.edge(x,y)
    g.view()


def main(argv=None):
    nodes = 200
    deep = 20
    degree = 20
    edges = gen_graph_deep(nodes, deep)
    graph_draw(range(nodes), edges, "deep")
    edges = gen_graph_degree(nodes, degree)
    graph_draw(range(nodes), edges, "degree")

if __name__ == "__main__":
    sys.exit(main())
