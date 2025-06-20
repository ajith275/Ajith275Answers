
import pandas as pd

df = pd.read_excel("sagatave_eksamenam.xlsx", sheet_name="Lapa_0")
df['Piegādes datums'] = pd.to_datetime(df['Piegādes datums'], errors='coerce')
q2 = df[(df['Prioritāte'] == 'High') & (df['Piegādes datums'].dt.year == 2015)]
print("Q2 Result:", len(q2))
