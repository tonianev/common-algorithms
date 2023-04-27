import heapq


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

    def dijkstra(self, start, end):
        queue = [(0, start)]
        visited = set()
        while queue:
            (cost, current) = heapq.heappop(queue)
            if current in visited:
                continue
            visited.add(current)
            if current == end:
                return cost
            for neighbor, weight in self.edges[current]:
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor))
        return -1
