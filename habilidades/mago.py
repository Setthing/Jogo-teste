import random


def ataque_normal_mago(jogador, inimigo):

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

def ataque_bola_de_fogo(jogador, inimigo):

    custo_mana = 30
    if jogador["mana"] < custo_mana:
        print("Mana insuficiente!")
        return
    
    jogador["mana"] -= custo_mana

    print("\nVocê lança uma bola de fogo!")
    fator = random.uniform(1.5, 2.0)
    dano_jogador = int((jogador["ataque"] - inimigo ["defesa"]) * fator)
    if dano_jogador < 0:
        dano_jogador = 0

    inimigo["vida"] -= dano_jogador

    if inimigo["vida"] < 0:
        inimigo["vida"] = 0

    print(f"Você causou {dano_jogador} de dano no {inimigo['nome']}")
    print(f"Vida do inimigo: {inimigo['vida']}\n")

def ataque_especial_meteorito(jogador, inimigo):

    custo_mana = 50
    if jogador["mana"] < custo_mana:
        print("Mana insuficiente!")
        return
    
    jogador["mana"] -= custo_mana

    print("\nVocê invoca um meteorito do céu!")
    fator = random.uniform(2.5, 3.0)
    dano_jogador = int((jogador["ataque"] - inimigo ["defesa"]) * fator)
    if dano_jogador < 0:
        dano_jogador = 0

    inimigo["vida"] -= dano_jogador

    if inimigo["vida"] < 0:
        inimigo["vida"] = 0

    print(f"Você causou {dano_jogador} de dano no {inimigo['nome']}")
    print(f"Vida do inimigo: {inimigo['vida']}\n")