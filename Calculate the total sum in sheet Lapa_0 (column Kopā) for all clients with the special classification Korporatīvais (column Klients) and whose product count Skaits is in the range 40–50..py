
import pandas as pd
import math

df = pd.read_excel("sagatave_eksamenam.xlsx", sheet_name="Lapa_0")
q5 = df[(df['Client'] == 'Corporate') & (df['Number'] >= 40) & (df['Number'] <= 50)]
q5_sum = math.floor(q5['Total'].sum())
print("Q5 Result:", q5_sum)
