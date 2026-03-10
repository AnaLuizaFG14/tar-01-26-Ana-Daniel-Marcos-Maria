import pandas as pd

anos = [2018,2019,2020,2021,2022,2023,2024,2025]

for ano in anos:
    df = pd.read_csv(f"Atracacao{ano}.csv") # lê o dataset
    df_filtro = df[df["Município"] == "Santos"]

    df_filtro.to_csv(f"Atracacao_santos{ano}.csv")
    print(ano,"\n")
    print(df_filtro)

print("fim")   

