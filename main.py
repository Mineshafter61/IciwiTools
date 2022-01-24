# This is a sample Python script.

import json
import math

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import getfromexcel
from dijkstra import *

fare_formula = lambda x: round((math.floor((2 * math.sqrt(math.floor(x / 100)) * 0.12) * 100)) / 100 + 0.6, 2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

  ### == INPUT == ###

  # lines = [[['Shinkura', 0.0], ['Sendagaya', 239.0], ['Asahi', 522.0], ['Kuroma', 874.0], ['Sakauji', 874.0], ['Nakano', 987.0], ['Sakae', 1158.0], ['University', 1339.0], ['Evertopia', 1453.0], ['SevenSisters', 1698.0], ['Downtown', 1851.0], ['LegacyRoad', 1947.0], ['Highgate', 2136.0], ['BartleyGate', 2313.0], ['MunicipalDistrict', 2484.0], ['RisingSun', 2628.0], ['LandsEnd', 2885.0], ['SeasEnd', 4603.0], ['Unnamed', 4851.0], ['EonRiver', 5119.0], ['EvernoteStreet', 5368.0], ['SolutionalPark', 5708.0], ['SunMoonLake', 6117.0]], [['LipanJunction', 0.0], ['EastEnd', 309.0], ['KewGardens', 493.0], ['ElmTreeCurve', 585.0], ['Riverside', 750.0], ['University', 924.0], ['PerryDistrict', 1038.0], ['Shortwood', 1804.0]], [['PelleJunction', 0.0], ['PelleEast', 299.0], ['EmmaruAquarium', 473.0], ['Nishibaru', 649.0], ['Tsurumai', 848.0], ['Shortwood', 1103.0], ['NewTraxia', 1243.0], ['Chiyoda', 1580.0]], [['SunMoonLake', 0.0], ['SolutionalPark', 429.0], ['EvernoteStreet', 774.0], ['EonRiver', 1023.0], ['Unnamed', 1261.0], ['SeasEnd', 1532.0], ['LandsEnd', 3192.0], ['RisingSun', 3449.0], ['MunicipalDistrict', 3593.0], ['BartleyGate', 3763.0], ['Highgate', 3941.0], ['LegacyRoad', 4129.0], ['Downtown', 4225.0], ['SevenSisters', 4381.0], ['Evertopia', 4630.0], ['University', 4744.0], ['Sakae', 4925.0], ['Nakano', 5096.0], ['Sakauji', 5255.0], ['Kuroma', 5255.0], ['Asahi', 5559.0], ['Sendagaya', 5839.0], ['Shinkura', 6078.0]], [['Shortwood', 0.0], ['PerryDistrict', 746.0], ['University', 860.0], ['Riverside', 1036.0], ['ElmTreeCurve', 1201.0], ['KewGardens', 1293.0], ['EastEnd', 1477.0], ['LipanJunction', 1777.0]], [['Chiyoda', 0.0], ['NewTraxia', 337.0], ['Shortwood', 477.0], ['Tsurumai', 732.0], ['Nishibaru', 931.0], ['EmmaruAquarium', 1107.0], ['PelleEast', 1281.0], ['PelleJunction', 1580.0]], [['LegacyRoad', 0.0], ['ProgressMonument', 494.0], ['MountVernon', 811.0], ['Castle', 1029.0], ['BartleyGate', 1372.0]], [['Rieryi', 0.0], ['EastEnd', 137.0], ['Rieryi', 274.0]], [['FlowerHill', 0.0], ['EmmaruWest', 393.0], ['EmmaruCentral', 606.0], ['EmmaruEast', 985.0], ['Gojo', 1247.0], ['Kyobashi', 1497.0], ['Sekisunahama', 1787.0], ['ShinseiDistrict', 2122.0], ['MizunaDistrict', 2325.0], ['DaitoDistrict', 2567.0], ['OtakiParkway', 2847.0], ['OtakiWaterfalls', 3120.0], ['ChinaTown', 3430.0], ['Gleisdreieck', 3742.0], ['Sendagaya', 4080.0], ['Shinkura', 4300.0], ['Suzume', 4570.0], ['Higurashi', 4841.0], ['MizunoPark', 5013.0], ['NorthAvenue', 5689.0]], [['EmmaruCentral', 0.0], ['Nishijima', 222.0], ['Karasuma4', 341.0], ['KarasumaCentre', 522.0], ['HanemiyaWest', 727.0], ['EmmaruAquarium', 898.0], ['Yachiyo', 1123.0], ['Kaname', 1339.0], ['LakeDistrict', 1545.0], ['Downtown', 1776.0], ['BushLane', 1968.0], ['ShafterGrove', 2099.0], ['TwinOaks', 2277.0], ['HeartDistrict', 2473.0]], [['EmmaruCentral', 0.0], ['Nihombashi', 181.0], ['Fukuno', 411.0], ['PortlandTunnel', 664.0], ['AjisaiTown', 954.0], ['Kusatsu', 1269.0], ['EnshimaBridge', 2214.0], ['SouthPoint', 3189.0]], [['NorthAvenue', 0.0], ['MizunoPark', 701.0], ['Higurashi', 868.0], ['Suzume', 1136.0], ['Shinkura', 1408.0], ['Sendagaya', 1628.0], ['Gleisdreieck', 1959.0], ['ChinaTown', 2274.0], ['OtakiWaterfalls', 2590.0], ['OtakiParkway', 2838.0], ['DaitoDistrict', 3135.0], ['MizunaDistrict', 3412.0], ['ShinseiDistrict', 3570.0], ['Sekisunahama', 3894.0], ['Kyobashi', 4182.0], ['Gojo', 4428.0], ['EmmaruEast', 4695.0], ['EmmaruCentral', 5077.0], ['EmmaruWest', 5286.0], ['FlowerHill', 5687.0]], [['SunMoonLake', 0.0], ['RoundTown', 303.0], ['Lakeside', 566.0], ['SolutionalPark', 1011.0], ['Newton', 1320.0], ['Flatlands', 1601.0], ['SunMoonLake', 1900.0]], [['SouthPoint', 0.0], ['EnshimaBridge', 975.0], ['Kusatsu', 1920.0], ['AjisaiTown', 2235.0], ['PortlandTunnel', 2525.0], ['Fukuno', 2778.0], ['Nihombashi', 3008.0], ['EmmaruCentral', 3189.0]], [['Lakeside', 0.0], ['SolutionalPark', 464.0], ['Chiaki', 700.0], ['MountLipan', 910.0], ['Inoriye', 1161.0], ['IslandTip', 1425.0]], [['SunMoonLake', 0.0], ['Flatlands', 302.0], ['Newton', 571.0], ['SolutionalPark', 877.0], ['Lakeside', 1320.0], ['RoundTown', 1599.0], ['SunMoonLake', 1919.0]], [['PelleJunction', 0.0], ['Amberside', 249.0], ['Kaname', 536.0], ['LakeSide', 663.0], ['ManumentBonk', 922.0], ['Southgate', 1092.0], ['SardEstates', 1218.0], ['Twee', 1384.0], ['Lighthouse', 1878.0]], [['IslandTip', 0.0], ['Inoriye', 262.0], ['MountLipan', 514.0], ['Chiaki', 722.0], ['SolutionalPark', 976.0], ['Lakeside', 1438.0]], [['HeartDistrict', 0.0], ['TwinOaks', 193.0], ['ShafterGrove', 376.0], ['BushLane', 507.0], ['Downtown', 699.0], ['LakeDistrict', 931.0], ['Kaname', 1138.0], ['Yachiyo', 1357.0], ['EmmaruAquarium', 1584.0], ['HanemiyaWest', 1755.0], ['KarasumaCentre', 1959.0], ['Karasuma4', 2141.0], ['Nishijima', 2259.0], ['EmmaruCentral', 2489.0]], [['Twee', 0.0], ['SardEstates', 190.0], ['Southgate', 316.0], ['ManumentBonk', 170.0], ['LakeSide', 730.0], ['Kaname', 869.0], ['Amberside', 1165.0], ['PelleJunction', 1406.0]], [['Yachiyo', 0.0], ['SakuramiTown', 221.0], ['Minowa', 390.0], ['LarcEnCiel', 481.0], ['SevenSisters', 639.0]], [['LipanCentral', 0.0], ['MarbleHouse', 326.0], ['Twee', 539.0], ['ChurchStreet', 642.0], ['LipanJunction', 780.0], ['BushLane', 1003.0], ['Downtown', 1194.0], ['LakeDistrict', 1415.0], ['Maybourne', 1625.0], ['LipanBusDepot', 1845.0], ['EvertopiaSouth', 1949.0], ['Tennoji', 2232.0], ['Shortwood', 2525.0], ['NewTraxiaCentral', 2705.0]], [['SevenSisters', 0.0], ['LarcEnCiel', 158.0], ['Minowa', 249.0], ['SakuramiTown', 418.0], ['Yachiyo', 639.0]], [['NewTraxiaCentral', 0.0], ['Shortwood', 184.0], ['Tennoji', 478.0], ['EvertopiaSouth', 731.0], ['LipanBusDepot', 858.0], ['Maybourne', 1079.0], ['LakeDistrict', 1296.0], ['Downtown', 1521.0], ['BushLane', 1712.0], ['LipanJunction', 1921.0], ['ChurchStreet', 2067.0], ['Twee', 2169.0], ['MarbleHouse', 2406.0], ['LipanCentral', 2732.0]]]
  lines = getfromexcel.run()

  graph = Graph()
  stations = []
  for line in lines:
    # lines is in the format [ [[station, cumulative distance], [station, cumulative distance]...], [[station, cumulative distance], [station, cumulative distance]...] ]
    for station_i in range(len(line) - 1):
      station_name = line[station_i][0]
      if station_name not in stations:
        stations.append(station_name)
      distance = line[station_i + 1][1] - line[station_i][1]
      next_station = line[station_i + 1][0]
      graph.addEdge(station_name, next_station, distance)

    [graph.addNode(s) for s in stations]

  ### == OUTPUT == ###

  final_dict = get_all_distances(graph, stations)
  for key in final_dict:
    for key1 in final_dict[key]:
      print(final_dict[key][key1])
      if final_dict[key][key1] >= 0:
        final_dict[key][key1] = fare_formula(final_dict[key][key1])  # apply fare formula
      else:
        final_dict[key][key1] = 'NaN'

  json_object = json.dumps(final_dict, indent=2)

  with open("fares.json", "w") as outfile:
    outfile.write(json_object)

  ### == GENERATE FARE CHARTS == ###

  # farecharts.run()
