import heapq
from collections import deque

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, source, target, weight):
        if source not in self.edges:
            self.edges[source] = []
        if target not in self.edges:
            self.edges[target] = []
        self.edges[source].append((target, weight))
        self.edges[target].append((source, weight))

    def a_star(self, start, end, heuristic):
        open_set = [(0, start, [])]
        visited = set()

        while open_set:
            (current_cost, current_node, path) = heapq.heappop(open_set)
            if current_node in visited:
                continue

            visited.add(current_node)
            path = path + [current_node]

            if current_node == end:
                return path

            for neighbor, weight in self.edges[current_node]:
                if neighbor not in visited:
                    estimated_cost = current_cost + weight + heuristic(neighbor, end)
                    heapq.heappush(open_set, (estimated_cost, neighbor, path))

        return None

# def euclidean_distance(a, b):
#     return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

# Note that the heuristic function you use should be tailored to the problem you're solving. 
# The sample provided calculates the Euclidean distance between two points, which is suitable for problems on a 2D plane.