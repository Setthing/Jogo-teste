
import random


def ataque_normal_assassino(jogador, inimigo):

    custo_mana = 0 # habilidade sem custo de mana
    if jogador["mana"] < custo_mana:
        print("Mana insuficiente!")
        return
    
    jogador["mana"] -= custo_mana #não vai mudar nada, mas é para manter a consistência com as outras habilidades

    print("\nVocê realiza um ataque normal!")
    fator = random.uniform(0.8, 1.2)
    dano_jogador = int((jogador["ataque"] - inimigo ["defesa"]) * fator)
    if dano_jogador < 0:
        dano_jogador = 0
    inimigo["vida"] -= dano_jogador
    if inimigo["vida"] < 0:
        inimigo["vida"] = 0
    print(f"Você causou {dano_jogador} de dano no {inimigo['nome']}")
    print(f"Vida do inimigo: {inimigo['vida']}\n")

def ataque_golpe_sombrio(jogador, inimigo):

    custo_mana = 40
    if jogador["mana"] < custo_mana:
        print("Mana insuficiente!")
        return
    
    jogador["mana"] -= custo_mana

    print("\nVocê realiza um golpe sombrio!")

    golpes = 3
    dano_total = 40
            
    if inimigo["vida"] <= 0:
        print("O inimigo já foi derrotado!")
        return
        
    fator = random.uniform(1.2, 1.6)
    dano_jogador = int((jogador["ataque"] - inimigo ["defesa"]) * fator)
    if dano_jogador < 0:
        dano_jogador = 1
    inimigo["vida"] -= dano_jogador
    if inimigo["vida"] < 0:
        inimigo["vida"] = 0
    print(f"Você causou {dano_jogador} de dano no {inimigo['nome']}")
    print(f"Vida do inimigo: {inimigo['vida']}\n")

def ataque_especial_veneno_mortal(jogador, inimigo):

    custo_mana = 60
    if jogador["mana"] < custo_mana:
        print("Mana insuficiente!")
        return
    
    jogador["mana"] -= custo_mana

    duracao_veneno = 3

    if "veneno" in inimigo["status"]:
            inimigo["status"]["veneno"] += duracao_veneno
    else:
            inimigo["status"]["veneno"] = duracao_veneno

    print("\nVocê aplica um veneno mortal por 3 turnos!")
    fator = random.uniform(2.5, 3.0)
    dano_jogador = int((jogador["ataque"] - inimigo ["defesa"]) * fator)
    if dano_jogador < 0:
        dano_jogador = 0
    inimigo["vida"] -= dano_jogador
    if inimigo["vida"] < 0:
        inimigo["vida"] = 0
    print(f"Você causou {dano_jogador} de dano no {inimigo['nome']}")
    print(f"Vida do inimigo: {inimigo['vida']}\n")