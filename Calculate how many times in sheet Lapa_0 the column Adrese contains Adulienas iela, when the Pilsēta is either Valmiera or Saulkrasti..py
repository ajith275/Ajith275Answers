
import pandas as pd

df = pd.read_excel("sagatave_eksamenam.xlsx", sheet_name="Lapa_0")
q3 = df[
    df['Adrese'].str.contains("Adulienas iela", na=False) &
    df['Pilsēta'].isin(["Valmiera", "Saulkrasti"])
]
print("Q3 Result:", len(q3))
