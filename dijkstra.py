from hashlist import *


def get_all_distances(hash_list: HashList):
  return_dict = {}
  for i in hash_list.index_list:
    return_dict[i] = dijkstra(hash_list, i)
  return return_dict


def dijkstra(hash_list: HashList, current: str):
  nodes = hash_list.index_list
  distances = {}
  for i in nodes:
    distances[hash_list.get_as_dict(i)[0]] = hash_list.get_as_dict(i)[1]
  # These are all the nodes which have not been visited yet
  unvisited = {node: None for node in nodes}
  # It will store the shortest distance from one node to another
  visited = {}
  # It will store the predecessors of the nodes
  current_distance = 0
  unvisited[current] = current_distance
  # Running the loop while all the nodes have been visited
  while True:
    # iterating through all the unvisited node
    for neighbour, distance in distances[current].items():
      # Iterating through the connected nodes of current_node (for
      # example, a is connected with b and c having values 10 and 3
      # respectively) and the weight of the edges
      if neighbour not in unvisited: continue
      new_distance = current_distance + distance
      if unvisited[neighbour] is None or unvisited[neighbour] > new_distance:
        unvisited[neighbour] = new_distance
    # Till now the shortest distance between the source node and target node
    # has been found. Set the current node as the target node
    visited[current] = current_distance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, current_distance = sorted(candidates, key=lambda x: x[1])[0]
  return visited


if __name__ == "__main__":
  h = HashList()
  h.insert(Node('B', 5, 'C'))
  h.insert(Node('A', 2, 'B'))
  h.insert(Node('A', 1, 'B'))
  h.insert(Node('A', 3, 'B'))
  h.insert(Node('C', 2, 'B'))
  h.insert(Node('C', 2, 'A'))
  h.debug()
  j = get_all_distances(h)
  for i in j:
    print(i, j[i])