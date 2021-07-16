file_name = input('File path: ')
sheet = 1

import pandas as pd
df = pd.read_excel(io=file_name, sheet_name=sheet)

lines_df = []
for i in range(10):
  lines_df.append(df.iloc[i*3, i*3:i*3+2].copy())
  
