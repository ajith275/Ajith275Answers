
import pandas as pd
import math

df = pd.read_excel("sagatave_eksamenam.xlsx", sheet_name="Lapa_0")
q4_df = df[df['Produkts'].str.contains("LaserJet", na=False)]
q4_avg = math.floor(q4_df['Cena'].mean())
print("Q4 Result:", q4_avg)
