import pandas as pd 

x = 2023

while x > 2009:

    df = pd.read_csv(f"{x}Atracacao.txt", sep=";", encoding="utf-8")

    df.to_csv(f"Atracacao{x}.csv",index=False)

    x-= 1

print("Feito")