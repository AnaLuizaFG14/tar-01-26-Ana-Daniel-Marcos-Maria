import pandas as pd

# filtragem dos dados por ano ou agrupado
resposta1 = str(input("Digite se quer pesquisar por ano: Sim/Não: ")).lower()

if resposta1 == "sim":
    ano = int(input("Digite o ano que quer pesquisar: "))
    df = pd.read_csv(f"Atracacao{ano}.csv")
else:
    df = pd.read_csv("dados_concatenados2024_2025.csv")


df_filtro = df[df["Município"] == "Santos"]

print(df_filtro)


reposta2 = str(input("Digite se quer salvar o dataset filtrado por Santos -> Sim/Não")).lower()

if reposta2 == "sim":
    df_filtro.to_csv(f"Dados_Filtrados_{ano}.csv",index=False)
    print("Dados salvo com sucesso")
else:
    print("Ação Terminada")