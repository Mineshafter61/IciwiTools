import pandas as pd


def main():
  df0 = pd.read_excel('TrainDistances.xlsx', sheet_name=0)
  df1 = pd.read_excel('TrainDistances.xlsx', sheet_name=1)
  df2 = pd.read_excel('TrainDistances.xlsx', sheet_name=2)
  lines = []
  for j in range(9):
    lines.append(df0.iloc[0:35, [j * 3, j * 3 + 1]])
    lines.append(df1.iloc[0:35, [j * 3, j * 3 + 1]])
    lines.append(df2.iloc[0:35, [j * 3, j * 3 + 1]])

  new_lines = list()
  for line in lines:
    records = line.to_dict('records')
    new_line = []
    for item in records:
      station = [item[key] for key in item]
      if type(station[0]) != float:
        print(station[0])
        name = station[0].replace(' ', '')
        distance = str(station[1])
        if distance.replace('.', '', 1).isdigit():  # check if float
          distance = float(distance)
          new_line.append([name, distance])

    if new_line:
      new_lines.append(new_line)

  return new_lines


if __name__ == '__main__':
  m = main()
  print(m)
  # for i in m:
  #   print(i)
