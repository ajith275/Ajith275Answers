
import pandas as pd

df = pd.read_excel("sagatave_eksamenam.xlsx", sheet_name="Lapa_0")
q1 = df[df['Adrese'].str.startswith("Ain", na=False) & (df['Count'] < 40)]
print("Q1 Result:", len(q1))
