import random
import pygame
import time

# ---------------- CONFIGURAÇÃO DE ÁUDIO ----------------
pygame.mixer.init()

# Função para carregar sons com segurança
def carregar_som(nome_arquivo):
    try:
        return pygame.mixer.Sound(nome_arquivo)
    except:
        print(f"⚠️ Alerta: Som '{nome_arquivo}' não encontrado.")
        return None

# Carregando seus arquivos exatos
som_galinha = carregar_som("galinha cacarejando.mp3")
som_passo = carregar_som("mudar de comomo.mp3")
som_vitoria = carregar_som("vitoria.mp3")
som_comodo = carregar_som("abertura de comodo.mp3") # Ajustado para o seu arquivo

def tocar_musica_fundo():
    try:
        pygame.mixer.music.load("abertura do game.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
    except:
        pass

# ---------------- DESENHOS (ASCII ART) ----------------
galinha = "\n    ,~.\n   (o o)\n  /  V  \\\n/(  _  )\\\n   ^^ ^^"
ovo_desenho = "\n    ___\n   /   \\\n  |     |\n   \\___/"
comodos_arte = {
    "cozinha": "[ COZINHA ]\n  _________\n |  FOGAO |\n |  _____ |\n | |     ||\n | |_____| \n |________|",
    "sala": "[ SALA ]\n  _________\n |  SOFA   |\n | [___]   |\n |  TV     |\n |_______  |",
    "quarto": "[ QUARTO ]\n  _________\n |  CAMA   |\n | [___]   |\n |       |\n |_______|",
    "banheiro": "[ BANHEIRO ]\n  _________\n | CHUVEIRO|\n |   🚿    |\n |   VASO   |\n |_________|",
    "varanda": "[ VARANDA ]\n  _________\n | PLANTAS |\n |   🌿🌿   |\n | CADEIRA |\n |_________|"
}

# ---------------- CONFIGURAÇÃO DO JOGO ----------------
comodos = list(comodos_arte.keys())
local_do_ovo = random.choice(comodos)
local_atual = "sala"
tentativas = 0

# ---------------- INÍCIO ----------------
tocar_musica_fundo()
print("🐔 Bem-vindo ao jogo: ONDE A GALINHA BOTOU O OVO?")
print(galinha)
if som_galinha: som_galinha.play()
time.sleep(1)

# ---------------- LOOP DO JOGO ----------------
while True:
    print("\n---------------------------------")
    print(f"Você está na {local_atual.upper()}.")
    print(comodos_arte[local_atual])

    print("\nPara onde deseja ir?")
    print(", ".join(comodos))

    escolha = input("👉 Digite o nome do cômodo: ").lower()
    
    if escolha not in comodos:
        print("❌ Cômodo inválido!")
        continue

    tentativas += 1
    local_atual = escolha
    
    # --- SONS DE TRANSIÇÃO ---
    if som_passo: som_passo.play()     # Som de passos/mudança
    time.sleep(0.5)                   # Pequena pausa dramática
    if som_comodo: som_comodo.play()   # SOM DE ABERTURA DO CÔMODO
    
    if local_atual == local_do_ovo:
        pygame.mixer.music.stop()
        if som_vitoria: som_vitoria.play()
        
        print("\n🎉 VOCÊ ENCONTROU O OVO!")
        print(ovo_desenho)
        print(f"🏆 Você encontrou em {tentativas} tentativas.")
        time.sleep(5) 
        break
    else:
        print("😕 Nada aqui... continue procurando.")