import pandas as pd
import json

result = {}
df = pd.read_excel(
  'Scoreboard Test.xlsx', 
  skiprows=[0, 5, 6],
  usecols=lambda c: not c.startswith('Unnamed:')
)

numCols = df.shape[1]

headers = df.iloc[:3]
data = df.iloc[3:]

for row in data.itertuples(index=True):
  date = row[1].strftime("%B %d, %Y")
  result[date] = []
  for i in range(1, numCols):
    col = headers.iloc[:, i]

    result[date].append({
      col.name: {
        "value": None if pd.isna(row[i+1]) else row[i+1],
        "focus": None if pd.isna(col[0]) else col[0],
        "source": None if pd.isna(col[1]) else col[1],
        "role": None if pd.isna(col[2]) else col[2]
      }
    })

with open("output.json", "w") as file:
  json.dump(result, file, default=str, indent=2)