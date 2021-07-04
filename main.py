# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from dijkstra import *
import json
import farecharts


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  h = HashList()


  ### == INPUT == ###

  lines = [ [['A', 0], ['B', 144]], [['C', 0], ['A', 222]] ]  #TODO: Excel opener

  for line in lines:
    # lines is in the format [ [[station, cumulative distance], [station, cumulative distance]...], [[station, cumulative distance], [station, cumulative distance]...] ]
    for station_i in range(len(line)-1):
      station_name = line[station_i][0]
      distance = line[station_i+1][1] - line[station_i][1]
      next_station = line[station_i+1][0]
      h.insert(Node(station_name, distance, next_station))
    h.clean()


  ### == OUTPUT == ###

  final_dict = get_all_distances(h)

  json_object = json.dumps(final_dict, indent=2)

  with open("fares.json", "w") as outfile:
    outfile.write(json_object)


  ### == GENERATE FARE CHARTS == ###

  farecharts.run()