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
