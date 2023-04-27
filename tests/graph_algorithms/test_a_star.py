import pytest
from src.graph_algorithms.a_star import Graph, euclidean_distance

def test_a_star():
    graph = Graph()
    graph.add_edge((0, 0), (0, 1), 1)
    graph.add_edge((0, 0), (1, 0), 1)
    graph.add_edge((1, 0), (1, 1), 1)
    graph.add_edge((0, 1), (1, 1), 1)

    path = graph.a_star((0, 0), (1, 1), euclidean_distance)
    assert path == [(0, 0), (1, 0), (1, 1)] or path == [(0, 0), (0, 1), (1, 1)]

    path = graph.a_star((0, 0), (0, 1), euclidean_distance)
    assert path == [(0, 0), (0, 1)]
