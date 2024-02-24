import pandas as pd     

df = pd.read_csv('big-mac-full-index.csv')

country = "Brazil"
query_text = f'name == "{country}" '

df_query = df.query(query_text)
print(df_query)






