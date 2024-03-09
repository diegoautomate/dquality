import pandas as pd
from faking import Faker
import random
from datetime import datetime, timedelta

# Inicializando o Faker para gerar dados fictícios
fake = Faker()

# Definindo o número de linhas na planilha
num_linhas = 100

# Lista para armazenar os dados
dados = []

# Gerando dados aleatórios para cada linha na planilha
for _ in range(num_linhas):
    id_ = fake.random_int(min=1000, max=9999)
    nome = fake.name()
    idade = fake.random_int(min=18, max=80)
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=80)
    email = fake.email()
    cargo = fake.job()
    departamento = fake.random_element(elements=('Vendas', 'TI', 'Marketing', 'RH', 'Financeiro'))

    dados.append([id_, nome, idade, data_nascimento, email, cargo, departamento])

# Criando um DataFrame pandas com os dados
df = pd.DataFrame(dados, columns=['id', 'nome', 'idade', 'datanascimento', 'email', 'cargo', 'departamento'])

# Salvando o DataFrame em um arquivo CSV
df.to_csv('planilha_dados_aleatorios.csv', index=False)

print("Planilha gerada com sucesso.")
