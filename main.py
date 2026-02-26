from personagem.criar_personagem import criar_personagem
from inimigos.goblin import criar_goblin
from combate.sistema_combate import iniciar_combate
from habilidades.goblin import ataque_normal_goblin, ataque_especial_goblin, defesa_goblin
from habilidades.guerreiro import ataque_normal_guerreiro, malha_de_escudos, ataque_especial_cortante
from habilidades.mago import ataque_normal_mago, ataque_bola_de_fogo, ataque_especial_meteorito
from habilidades.assassino import ataque_normal_assassino, ataque_golpe_sombrio, ataque_especial_veneno_mortal
from habilidades.paladino import ataque_normal_paladino, curar_paladino, ataque_especial_luz_sagrada
from habilidades.necromante import ataque_normal_necromante, ataque_toque_da_morte, ataque_especial_rainha_dos_mortos


#Criar Personagem
jogador = criar_personagem()

#Criar Inimigo
goblin = criar_goblin()

#Iniciar Combate
iniciar_combate(jogador, goblin)