
from random import random


def ataque_normal_necromante(jogador, inimigo):

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

def ataque_toque_da_morte(jogador, inimigo):
    
    custo_mana = 30
    if jogador["mana"] < custo_mana:
        print("Mana insuficiente!")
        return
    
    jogador["mana"] -= custo_mana

    print("\nVocê realiza um ataque de toque da morte!")
    fator = random.uniform(1.5, 2.0)
    dano_jogador = int((jogador["ataque"] - inimigo ["defesa"]) * fator)
    if dano_jogador < 0:
        dano_jogador = 0

    inimigo["vida"] -= dano_jogador

    if inimigo["vida"] < 0:
        inimigo["vida"] = 0

    print(f"Você causou {dano_jogador} de dano no {inimigo['nome']}")
    print(f"Vida do inimigo: {inimigo['vida']}\n")

def ataque_especial_rainha_dos_mortos(jogador, inimigo):

    custo_mana = 50
    if jogador["mana"] < custo_mana:
        print("Mana insuficiente!")
        return
    
    jogador["mana"] -= custo_mana

    jogador["invocacao"] = {
        "nome": "Rainha dos Mortos",
        "turnos_restantes": 3,
        "ataque": int(jogador["ataque"] * 0.8)
    }

    print("\nVocê invoca a rainha dos mortos para atacar!")
    fator = random.uniform(2.5, 3.0)
    dano_jogador = int((jogador["ataque"] - inimigo ["defesa"]) * fator)
    if dano_jogador < 0:
        dano_jogador = 0

    inimigo["vida"] -= dano_jogador

    if inimigo["vida"] < 0:
        inimigo["vida"] = 0

    print(f"Você causou {dano_jogador} de dano no {inimigo['nome']}")
    print(f"Vida do inimigo: {inimigo['vida']}\n")