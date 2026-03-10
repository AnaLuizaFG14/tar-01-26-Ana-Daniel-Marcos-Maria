import pandas as pd

dataset_2024 = pd.read_csv("Atracacao2024.csv")

dataset_2025 = pd.read_csv("Atracacao2025.csv")

df_final = pd.concat([dataset_2024,dataset_2025],axis=0)

df_final.reset_index(drop=True,inplace=True)

df_final.to_csv("dados_concatenados2024_2025.csv",index=False)

print(df_final)

