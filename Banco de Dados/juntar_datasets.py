import pandas as pd

anos = [2018,2019,2020,2021,2022,2023,2024,2025]

dataset_2018 = pd.read_csv("Atracacao_santos2018.csv")

dataset_2019 = pd.read_csv("Atracacao_santos2019.csv")

dataset_2020 = pd.read_csv("Atracacao_santos2020.csv")

dataset_2021 = pd.read_csv("Atracacao_santos2021.csv")

dataset_2022 = pd.read_csv("Atracacao_santos2022.csv")

dataset_2023 = pd.read_csv("Atracacao_santos2023.csv")

dataset_2024 = pd.read_csv("Atracacao_santos2024.csv")

dataset_2025 = pd.read_csv("Atracacao_santos2025.csv")

df_final = pd.concat([dataset_2018,dataset_2019,dataset_2020,dataset_2021,dataset_2022,dataset_2023,dataset_2024,dataset_2025],axis=0)

df_final.reset_index(drop=True,inplace=True)

df_final.to_csv("dados_concatenados_santos2018_2025.csv",index=False)

print(df_final)

