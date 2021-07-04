import json
from PIL import Image, ImageFont, ImageDraw
from re import finditer


def camel_case_split(identifier):
  matches = finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
  thing = ' '.join([m.group(0) for m in matches])
  for char in thing:
    if char in '1234567890': thing = thing[0:-1]+' District '+char
  # Special cases
  if thing == 'Prog Monument': return 'Progress Monument'
  return thing


def run():
  with open("fares.json", "r") as fare_file:
    fares = json.load(fare_file)
  for startStation in fares:
    font_small = ImageFont.truetype('/Library/Fonts/font_1_honokamarugo_1.1.ttf', 30)
    font_big = ImageFont.truetype('/Library/Fonts/font_1_honokamarugo_1.1.ttf', 90)
    end_stations = [i for i in fares[startStation]]
    index = 0
    page = 1
    while index < len(end_stations):
      header_format = camel_case_split(startStation) if len(end_stations) <= 260 else camel_case_split(startStation) + " (" + str(page) + ")"
      filename = startStation if len(end_stations) <= 260 else startStation + "_" + page
      canvas = Image.open("./img/__BLANK.png")
      d = ImageDraw.Draw(canvas)
      d.text((1280, 224), header_format, font=font_big, fill=(0, 0, 0), anchor='ms')
      j_tuple = 69, 669, 1269, 1869, 2469
      jj = 0
      while jj < len(j_tuple) and index < len(end_stations):
        j = j_tuple[jj]
        i = 420
        while i < 2461 and index < len(end_stations):
          d.text((j, i), "{0}".format(camel_case_split(end_stations[index])), font=font_small, fill=(0, 0, 0))
          d.text((j + 351, i), "£{0}".format(fares[startStation][end_stations[index]]), font=font_small,
                 fill=(0, 0, 0))
          i += 40
          index += 1
        jj += 1
      canvas.save('./img/{0}.png'.format(filename).replace(" ", ""))
      page += 1
    print(startStation + ' processed!')
