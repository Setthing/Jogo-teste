import random

def ataque_normal_paladino(jogador, inimigo):

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

def curar_paladino(jogador, inimigo):

    custo_mana = 20
    if jogador["mana"] < custo_mana:
        print("Mana insuficiente!")
        return
    
    jogador["mana"] -= custo_mana

    print("\nVocê se cura!")
    jogador["vida"] += 30
    if jogador["vida"] > jogador["vida_maxima"]:
        jogador["vida"] = jogador["vida_maxima"]
    print(f"Sua vida agora é {jogador['vida']}")

def ataque_especial_luz_sagrada(jogador, inimigo):

    custo_mana = 50
    if jogador["mana"] < custo_mana:
        print("Mana insuficiente!")
        return
    
    jogador["mana"] -= custo_mana
    
    print("\nVocê invoca a luz sagrada para atacar!")
    fator = random.uniform(2.5, 3.0)
    dano_jogador = int((jogador["ataque"] - inimigo ["defesa"]) * fator)
    if dano_jogador < 0:
        dano_jogador = 0

    inimigo["vida"] -= dano_jogador

    if inimigo["vida"] < 0:
        inimigo["vida"] = 0

    print(f"Você causou {dano_jogador} de dano no {inimigo['nome']}")
    print(f"Vida do inimigo: {inimigo['vida']}\n")