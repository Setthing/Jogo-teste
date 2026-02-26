from random import random


def ataque_normal_guerreiro(jogador, inimigo):

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

def malha_de_escudos(jogador, inimigo):

    custo_mana = 20
    if jogador["mana"] < custo_mana:
        print("Mana insuficiente!")
        return
    
    jogador["mana"] -= custo_mana

    print("\nVocê ativa a malha de escudos, aumentando sua defesa!")
    jogador["defesa"] += 5
    print(f"Sua defesa aumentou para {jogador['defesa']} por 3 turnos!\n")

def ataque_especial_cortante(jogador, inimigo):

    custo_mana = 40
    if jogador["mana"] < custo_mana:
        print("Mana insuficiente!")
        return
    
    jogador["mana"] -= custo_mana
    
    print("\nVocê realiza um ataque especial!")
    fator = random.uniform(2.5, 3.0)
    dano_jogador = int((jogador["ataque"] - inimigo ["defesa"]) * fator)
    if dano_jogador < 0:
        dano_jogador = 0

    inimigo["vida"] -= dano_jogador

    if inimigo["vida"] < 0:
        inimigo["vida"] = 0

    print(f"Você causou {dano_jogador} de dano no {inimigo['nome']}")
    print(f"Vida do inimigo: {inimigo['vida']}\n")