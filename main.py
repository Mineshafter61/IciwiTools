# This is a sample Python script.

import json
import math

import farecharts
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import getfromexcel
from dijkstra import *

fare_formula = lambda x: round((math.floor((2 * math.sqrt(math.floor(x / 100)) * 0.12) * 100)) / 100 + 0.6, 2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  h = HashList()

  ### == INPUT == ###

  # lines = [ [['A', 0], ['B', 144]], [['C', 0], ['A', 222]] ]
  lines = getfromexcel.main()

  for line in lines:
    # lines is in the format [ [[station, cumulative distance], [station, cumulative distance]...], [[station, cumulative distance], [station, cumulative distance]...] ]
    for station_i in range(len(line) - 1):
      station_name = line[station_i][0]
      distance = line[station_i + 1][1] - line[station_i][1]
      next_station = line[station_i + 1][0]
      h.insert(Node(station_name, distance, next_station))
    h.clean()

  ### == OUTPUT == ###

  final_dict = get_all_distances(h)
  for key in final_dict:
    for key1 in final_dict[key]:
      final_dict[key][key1] = fare_formula(final_dict[key][key1])  # apply fare formula

  json_object = json.dumps(final_dict, indent=2)

  with open("fares.json", "w") as outfile:
    outfile.write(json_object)

  ### == GENERATE FARE CHARTS == ###

  farecharts.run()
