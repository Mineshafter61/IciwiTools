from collections import defaultdict


# Initializing the Graph Class
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def addNode(self, value):
    self.nodes.add(value)

  def addEdge(self, fromNode, toNode, distance):
    self.edges[fromNode].append(toNode)
    self.distances[(fromNode, toNode)] = distance


def get_all_distances(graph: Graph, stations: list):
  r = {}
  for station in stations:
    g = dijkstra(graph, station)
    r[station] = g[0]
  return r


# Implementing Dijkstra's Algorithm
def dijkstra(graph, initial):
  visited = {initial: 0}
  path = defaultdict(list)

  nodes = set(graph.nodes)

  while nodes:
    minNode = None
    for node in nodes:
      if node in visited:
        if minNode is None:
          minNode = node
        elif visited[node] < visited[minNode]:
          minNode = node
    if minNode is None:
      break

    nodes.remove(minNode)
    currentWeight = visited[minNode]

    for edge in graph.edges[minNode]:
      weight = currentWeight + graph.distances[(minNode, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge].append(minNode)

  return visited, path


if __name__ == "__main__":
  pass
