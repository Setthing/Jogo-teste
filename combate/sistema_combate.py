import random


def iniciar_combate(jogador, inimigo):
    
    print(f"\n⚔ Um {inimigo['nome']} aparece! Prepare-se para o combate! ⚔\n")

    while jogador["vida"] > 0 and inimigo["vida"] > 0:

        # Turno do Jogador

        fator = random.uniform(0.8, 1.2)
        dano_jogador = int((jogador["ataque"] - inimigo ["defesa"]) * fator)
        if dano_jogador < 0:
            dano_jogador = 0

        inimigo["vida"] -= dano_jogador

        if inimigo["vida"] < 0:
            inimigo["vida"] = 0

        print(f"Você causou {dano_jogador} de dano no {inimigo['nome']}")
        print(f"Vida do inimigo: {inimigo['vida']}\n")

        if inimigo["vida"] <= 0:
            print (f"Parabéns! Você derrotou o {inimigo['nome']}!")
            break
        # Turno do Inimigo

        if "veneno" in inimigo["status"]:

            dano_veneno = int(jogador["vida"] * 0.3)

            inimigo["vida"] -= dano_veneno

            print(f"O {inimigo['nome']} sofre {dano_veneno} de dano por causa do veneno!")
            print(f"Vida do inimigo: {inimigo['vida']}\n")

            inimigo["status"]["veneno"] -= 1

            if inimigo["status"]["veneno"] <= 0:
                del inimigo["status"]["veneno"]
                print(f"O veneno no {inimigo['nome']} acabou!\n")

        if inimigo["vida"] <= 0:
            print (f"Parabéns! Você derrotou o {inimigo['nome']}!")
            break

        fator = random.uniform(0.4, 0.9)
        dano_inimigo = int((inimigo["ataque"] - jogador["defesa"]) * fator)
        if dano_inimigo < 0: 
            dano_inimigo = 0

        jogador["vida"] -= dano_inimigo

        if jogador["vida"] < 0:
            jogador["vida"] = 0

        print(f"O {inimigo['nome']} causou {dano_inimigo} de dano em você!")
        print(f"Sua vida: {jogador['vida']}\n")
        if jogador["vida"] <= 0:
            print(f"Você foi derrotado pelo {inimigo['nome']}! Tente novamente!")
            break