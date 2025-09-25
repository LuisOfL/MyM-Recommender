import pandas as pd
import os

ruta_csv = os.path.join(os.path.dirname(__file__), "movies_metadata.csv")
df = pd.read_csv(ruta_csv)

df_new = df[['title']]
df_new.to_csv("titles.csv", index=False)
print(df_new)