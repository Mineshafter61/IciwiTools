import json

if __name__ == '__main__':
  print('\nZone names will be in the format <operator><zone> if this is set to true.')
  multiple_operators = True if input('Allow multiple operators? [Y/N] ').lower() == 'y' else False

  final_dict = {}

  # multiple operators
  if multiple_operators:
    s = int(input('\nKey in the number of operators: '))
    operator_list = [input('Name of operator #{}: '.format(i + 1)) for i in range(s)]

    for operator in operator_list:
      # additional settings for operator
      print('\n**********\nThe following settings are for the operator {}.'.format(operator))
      print('Key in the number of zones.')
      zones = int(input('Number of zones: '))
      print('Lettered zones are in the format A1, A2, A3...')
      letter_zones = True if input('Use lettered zones? [Y/N] ').lower() == 'y' else False
      print('Sub-zones are used to determine whether a trip was made through the central zone.\n' +
            'If the starting and ending sub-zones do not match, the trip is taken to have gone through the central zone.')
      sub_zones = int(input('Number of sub-zones: '))

      # key in fare values
      print('\nThe following settings are for train fares between each zone.')
      for i in range(1, zones + 1):
        for j in range(1, zones + 1):
          if letter_zones:
            i_, j_ = chr(64 + i), chr(64 + j)
          else:
            i_, j_ = str(i), str(j)

          within = float(input('\nWITHIN SUB-ZONES fare from Zone {0} -> Zone {1}: '.format(i_, j_)))
          across = float(input('ACROSS SUB-ZONES fare from Zone {0} -> Zone {1}: '.format(i_, j_)))

          # sub-zones
          for s in range(1, sub_zones + 1):
            if letter_zones and (operator + i_ + str(s)) not in final_dict:
              final_dict[operator + i_ + str(s)] = {}
            elif not letter_zones and (operator + i_ + chr(96 + s)) not in final_dict:
              final_dict[operator + i_ + chr(96 + s)] = {}

            for t in range(1, sub_zones + 1):
              if letter_zones:
                if s == t:  # same sub-zone
                  final_dict[operator + i_ + str(s)][operator + j_ + str(t)] = within
                else:
                  final_dict[operator + i_ + str(s)][operator + j_ + str(t)] = across
              else:
                if s == t:  # same sub-zone
                  final_dict[operator + i_ + chr(96 + s)][operator + j_ + chr(96 + t)] = within
                else:
                  final_dict[operator + i_ + chr(96 + s)][operator + j_ + chr(96 + t)] = across



  # single operator
  else:
    print('Key in the number of zones.')
    zones = int(input('Number of zones: '))
    print('Lettered zones are in the format A1, A2, A3...')
    letter_zones = True if input('Use lettered zones? [Y/N] ').lower() == 'y' else False
    print('Sub-zones are used to determine whether a trip was made through the central zone.\n' +
          'If the starting and ending sub-zones do not match, the trip is taken to have gone through the central zone.')
    sub_zones = int(input('Number of sub-zones: '))

    print('\nThe following settings are for train fares between each zone.')
    for i in range(1, zones + 1):
      for j in range(1, zones + 1):
        if letter_zones:
          i_, j_ = chr(64 + i), chr(64 + j)
        else:
          i_, j_ = str(i), str(j)

        within = float(input('\nWITHIN SUB-ZONES fare from Zone {0} -> Zone {1}: '.format(i_, j_)))
        across = float(input('ACROSS SUB-ZONES fare from Zone {0} -> Zone {1}: '.format(i_, j_)))

        # sub-zones
        for s in range(1, sub_zones + 1):
          if letter_zones and (i_ + str(s)) not in final_dict:
            final_dict[i_ + str(s)] = {}
          elif not letter_zones and (i_ + chr(96 + s)) not in final_dict:
            final_dict[i_ + chr(96 + s)] = {}

          for t in range(1, sub_zones + 1):
            if letter_zones:
              if s == t:  # same sub-zone
                final_dict[i_ + str(s)][j_ + str(t)] = within
              else:
                final_dict[i_ + str(s)][j_ + str(t)] = across
            else:
              if s == t:  # same sub-zone
                final_dict[i_ + chr(96 + s)][j_ + chr(96 + t)] = within
              else:
                final_dict[i_ + chr(96 + s)][j_ + chr(96 + t)] = across

  json_object = json.dumps(final_dict, indent=2)
  print('\nAll values recorded in fares.json.')

  with open("fares.json", "w") as outfile:
    outfile.write(json_object)
