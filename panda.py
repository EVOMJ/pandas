## Exercício 1
# Crie um DataFrame simples com 3 colunas e 5 linhas.

import pandas as pd

dados = {'nome': ['Alice', 'Bob', 'Charlie'],
        'Idade': [25, 30, 35],
        'cidade': ['New York', 'London', 'Paris']}
df = pd.DataFrame(dados)
df


## Exercício 2
# Carregue um arquivo CSV (pode ser inventado) usando `pd.read_csv()`.
import pandas as pd

dados = {'nome': ['Alice', 'Bob', 'Charlie'],
        'Idade': [25, 30, 35],
        'cidade': ['New York', 'London', 'Paris']}
# Criar um DataFrame
df = pd.DataFrame(dados)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('pessoas.csv', index=False)

# Carregar o CSV de volta
df_carregado = pd.read_csv('pessoas.csv')
print(df_carregado)

# ## Exercício 3
# Mostre as primeiras 3 linhas com `.head()`.

import pandas as pd

# Example data
data = {
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Idade': [25, 30, 35],
    'Cidade': ['New York', 'London', 'Paris']
}

# Creating DataFrame
df = pd.DataFrame(data)

# Using head() method on DataFrame
print(df.head(2))


# ## Exercício 4
# Mostre as informações do DataFrame com `.info()`.
import pandas as pd

data = {
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Idade': [25, 30, 35],
    'Cidade': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)

print(df.info(3))










