import random

def ataque_normal_goblin(jogador, inimigo):
    print("\nO Goblin realiza um ataque normal!")
    fator = random.uniform(0.8, 1.2)
    dano_inimigo = int((inimigo["ataque"] - jogador ["defesa"]) * fator)
    if dano_inimigo < 0:
        dano_inimigo = 0

    jogador["vida"] -= dano_inimigo

    if jogador["vida"] < 0:
        jogador["vida"] = 0

    print(f"O Goblin causou {dano_inimigo} de dano em você!")
    print(f"Sua vida: {jogador['vida']}\n")

def ataque_especial_goblin(jogador, inimigo):
    print("\nO Goblin realiza um ataque especial!")
    fator = random.uniform(1.5, 2.0)
    dano_inimigo = int((inimigo["ataque"] - jogador ["defesa"]) * fator)
    if dano_inimigo < 0:
        dano_inimigo = 0

    jogador["vida"] -= dano_inimigo

    if jogador["vida"] < 0:
        jogador["vida"] = 0

    print(f"O Goblin causou {dano_inimigo} de dano em você!")
    print(f"Sua vida: {jogador['vida']}\n")

def defesa_goblin(jogador, inimigo):
    print("\nO Goblin se defende, aumentando sua defesa!")
    inimigo["defesa"] += 30
    print(f"A defesa do Goblin aumentou para {inimigo['defesa']} por 3 turnos!\n")