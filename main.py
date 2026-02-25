from personagem.criar_personagem import criar_personagem
from inimigos.goblin import criar_goblin
from combate.sistema_combate import iniciar_combate


#Criar Personagem
jogador = criar_personagem()

#Criar Inimigo
goblin = criar_goblin()

#Iniciar Combate
iniciar_combate(jogador, goblin)