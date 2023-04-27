import pytest
from src.graph_algorithms.dijkstra import Graph

def test_dijkstra():
    graph = Graph()
    graph.add_edge("A", "B", 7)
    graph.add_edge("A", "C", 9)
    graph.add_edge("A", "F", 14)
    graph.add_edge("B", "C", 10)
    graph.add_edge("B", "D", 15)
    graph.add_edge("C", "D", 11)
    graph.add_edge("C", "F", 2)
    graph.add_edge("D", "E", 6)
    graph.add_edge("E", "F", 9)

    assert graph.dijkstra("A", "E") == 20
    assert graph.dijkstra("A", "F") == 11
    assert graph.dijkstra("A", "C") == 9
    assert graph.dijkstra("A", "A") == 0
