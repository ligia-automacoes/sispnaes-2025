import pandas as pd

PATH = "C:\\Users\\joaor\\OneDrive\\Documents\\IF\\sispnaes-2025\\Despesas com Assistência Estudantil 2025 (apenas Bolsas).csv"

df = pd.read_csv(
    PATH,
    sep="\t",
    encoding="cp1252",
    skiprows=4
)

# print(df.head(10))

# print(df.describe())

df.shape
linhas, colunas = df.shape[0], df.shape[1]
print("linhas:", linhas)
print("colunas:", colunas)
print(df.describe())
