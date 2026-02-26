def criar_personagem():
    nome = input("Digite o nome do seu Personagem: ")

    print("Escolha sua classe: ")
    print("1 - Guerreiro")
    print("2 - Mago")
    print("3 - Arqueiro")
    print("4 - Paladino")
    print("5 - Assassino")
    print("6 - Necromante")

    classe = input("Digite o nome da classe escolhida: ").lower()

    if classe == "guerreiro":
        print(f"{nome} é um Guerreiro!")
        vida = 180
        vida_max = 180
        mana = 50
        mana_max = 50
        ataque = 25
        defesa = 20
        tipo_ataque = "Espada"
        tipo = "Pesado"


    elif classe == "paladino":
        print(f"{nome} é um Paladino!")
        vida = 200
        vida_max = 200
        mana = 80
        mana_max = 80
        ataque = 20
        defesa = 25
        tipo_ataque = "Martelo"
        tipo = "Pesado"

    elif classe == "mago":
        print(f"{nome} é um Mago!")
        vida = 120
        vida_max = 120
        mana = 100
        mana_max = 100
        ataque = 30
        defesa = 15
        tipo_ataque = "Magia"
        tipo = "Medio"

    elif classe == "necromante":
        print(f"{nome} é um Necromante!")
        vida = 100
        vida_max = 100
        mana = 120
        mana_max = 120
        ataque = 35
        defesa = 20
        tipo_ataque = "Magia Negra"
        tipo = "Medio"

    elif classe == "arqueiro":
        print(f"{nome} é um Arqueiro!")
        vida = 80
        vida_max = 80
        mana = 60
        mana_max = 60
        ataque = 45
        defesa = 10
        tipo_ataque = "Arco e Flecha"
        tipo = "Leve"

    elif classe == "assassino":
        print(f"{nome} é um Assassino!")
        vida = 90
        vida_max = 90
        mana = 70
        mana_max = 70
        ataque = 40
        defesa = 15
        tipo_ataque = "Adaga"
        tipo = "Leve"

    else:
        print("Classe inválida! Por favor, escolha uma classe válida.")
        exit()

    print("\n=== Personagem Criado ===")
    print(f"Nome: {nome}")
    print(f"Classe: {classe.title()}")
    print(f"Vida: {vida}")
    print(f"Ataque: {ataque}")
    print(f"Defesa: {defesa}")
    print(f"Tipo de Ataque: {tipo_ataque}")
    print(f"Tipo: {tipo}")

    jogador = {
        "nome": nome,
        "classe": classe,
        "vida": vida,
        "ataque": ataque,
        "defesa": defesa,
        "tipo_ataque": tipo_ataque,
        "tipo": tipo
    }

    return jogador