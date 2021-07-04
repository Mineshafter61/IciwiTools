class Node:
  next_station: str
  station: str
  distance: float

  def __init__(self, station=None, distance=None, next_station=None):
    self.station = station
    self.distance = distance
    self.next_station = next_station

  def is_null(self):
    return self.station is None and self.distance is None and self.next_station is None


class HashList:
  hash_list: list[list[Node]]
  index_list: list[str]

  def __init__(self):
    self.hash_list = []
    self.index_list = []

  # hash_list: [[node, node, node],[node,node,node]]

  def insert(self, node: Node):
    if node.station not in self.index_list:
      # new station
      i = 0
      # order station by alphabetical order
      while i < len(self.index_list) and self.index_list[i] < node.station:
        i += 1
      self.index_list.insert(i, node.station)
      self.hash_list.insert(i, [node])

    else:
      # check for duplicates
      i = self.index_list.index(node.station)
      flag = True
      for stored_node in self.hash_list[i]:
        if stored_node.station == node.station and stored_node.next_station == node.next_station and stored_node.distance > node.distance:
          # override distance
          stored_node.distance = node.distance
          # don't insert
          # set flag
          flag = False
        elif stored_node.station == node.station and stored_node.next_station == node.next_station:
          # stored_node.distance is smaller than node.distance, so we do not insert, instead we just set the flag
          flag = False

      if flag:
        # if it's not a new station, just append
        i = self.index_list.index(node.station)
        self.hash_list[i].append(node)

  def debug(self):
    print(self.index_list)
    for row in self.hash_list:
      for node in row:
        print(node.station,node.distance, node.next_station, end=" | ")
      print()

  def __getitem__(self, item):
    if type(item == str):
      return self.hash_list[self.index_list.index(item)]
    else:
      return self.hash_list[item]

  def get_as_dict(self, item):
    if type(item == str):
      new_dict = {}
      station = ''
      for i in self.hash_list[self.index_list.index(item)]:
        station = i.station
        new_dict[i.next_station] = i.distance
      return station, new_dict

  def clean(self):
    to_remove = []
    for station_list_i in range(len(self.hash_list)):
      processed_next_stations = []
      for node_i in range(len(self.hash_list[station_list_i])):
        if self.hash_list[station_list_i][node_i].next_station not in processed_next_stations:
          processed_next_stations.append(self.hash_list[station_list_i][node_i].next_station)
        else:
          # duplicate found
          distance = self.hash_list[station_list_i][node_i].distance
          for node_j in range(len(self.hash_list[station_list_i])):
            if self.hash_list[station_list_i][node_j].distance <= distance:
              # remove current node
              to_remove.append((station_list_i, node_i))
              break
            else:
              # remove that node
              to_remove.append((station_list_i, node_j))
              break
    for each in to_remove:
      self.hash_list[each[0]][each[1]] = Node()

    self.hash_list = [[node for node in station if not node.is_null()] for station in self.hash_list]
    return self.hash_list