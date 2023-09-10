
# DIO | Projeto NPC Generator

Esse repositório tem como finalidade a aprendizagem e estudo de importação de dados .csv utilizando a linguagem Python, também contribuindo com o projeto do curso de **Introdução à Ciência de Dados com Python** da [Digital Innovation One](https://www.dio.me/).

Trata-se de um simples programa que gera uma quantidade definida pelo usuário de personagens de RPG aleatórios, onde se estrai os dados principais de um arquivo csv, os randomizam e exeportam para outro aquivo csv.

Por se tratar de um reposítorio para estudos, o projeto fica aberto para quem quiser clona-lo e estuda-lo.

## Foram utilizados nesse projeto:

- **linguagem** -> Python 3
- **Bibliotecas** -> *pandas* e *random*
- **Interpretador** -> VSC (Visual Estudio Code)
- **Git** para importação do repositório

## 📚 Documentação
- [Documentação Git](https://git-scm.com/doc)
- [Documentação GitHub](https://docs.github.com/)
- [Documentação Pandas](https://pandas.pydata.org/docs/)
- [Documentação Python](https://docs.python.org/3/)

```
import pandas as pd
import random

# Lê as informações do arquivo CSV
informacoes = pd.read_csv('npc_info.csv')

# Filtra os valores válidos para cada lista
npc_nome_masculino = informacoes["name_m"].dropna().tolist()
npc_nome_feminino = informacoes["name_f"].dropna().tolist()
npc_raca = informacoes["race"].dropna().tolist()
npc_classe = informacoes["class"].dropna().tolist()
npc_alinhamento = informacoes["alignment"].dropna().tolist()
npc_genero = informacoes["gender"].dropna().tolist()

# Verifica se as listas estão vazias após a filtragem
if not all([npc_nome_masculino, npc_nome_feminino, npc_raca, npc_classe, npc_alinhamento, npc_genero]):
    print("Alguma das listas está vazia após a filtragem. Verifique seu arquivo CSV.")
else:
    quantidade_npc = int(input("Digite quantos npcs deseja gerar: "))  # Converte para inteiro
    if quantidade_npc <= 0:
        print("A quantidade deve ser maior que zero.")
    else:
        # Crie uma lista para armazenar os personagens gerados
        personagens = []
        
        for _ in range(quantidade_npc):
            # Escolha aleatoriamente um elemento de cada lista
            genero_aleatorio = random.choice(npc_genero)
            
            if genero_aleatorio == "Masculino":
                nome_aleatorio = random.choice(npc_nome_masculino)
            elif genero_aleatorio == "Feminino":
                nome_aleatorio = random.choice(npc_nome_feminino)
            else:
                nome_aleatorio = "Nome Genérico"  # Você pode definir um nome genérico ou tratamento para outros gêneros
            
            raca_aleatoria = random.choice(npc_raca)
            classe_aleatoria = random.choice(npc_classe)
            alinhamento_aleatorio = random.choice(npc_alinhamento)
            
            # Crie um dicionário para cada personagem
            personagem = {
                "Gênero": genero_aleatorio,
                "Nome": nome_aleatorio,
                "Raça": raca_aleatoria,
                "Classe": classe_aleatoria,
                "Alinhamento": alinhamento_aleatorio,
            }
            
            # Adicione o personagem à lista
            personagens.append(personagem)
        
        # Crie um DataFrame do pandas a partir da lista de personagens
        df = pd.DataFrame(personagens)
        
        # Exporte o DataFrame para um arquivo CSV
        df.to_csv('npc_list.csv', index=False)

        print(f"{quantidade_npc} personagens foram exportados para npc_list.csv.")

```