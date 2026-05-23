import random
import pygame
import time

# ---------------- CONFIGURAÇÃO DE CORES (ANSI) ----------------
RESET = "\033[0m"
NEGRITO = "\033[1m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
CIANO = "\033[36m"
MAGENTA = "\033[35m"
CINZA = "\033[90m"

# ---------------- CONFIGURAÇÃO DE ÁUDIO ----------------
pygame.mixer.init()

def carregar_som(nome_arquivo):
    try:
        return pygame.mixer.Sound(nome_arquivo)
    except:
        return None

# Carregando seus arquivos exatos
som_galinha = carregar_som("galinha cacarejando.mp3")
som_passo = carregar_som("mudar de comomo.mp3")
som_vitoria = carregar_som("vitoria.mp3")
som_comodo = carregar_som("abertura de comodo.mp3")
som_gameover = carregar_som("game over.mp3")

def tocar_musica_fundo():
    try:
        pygame.mixer.music.load("abertura do game.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1) # Toca em loop
    except:
        pass

# ---------------- ARTES ASCII DETALHADAS ----------------

galinha_art = f"""{AMARELO}
      //\\
     ((o o))  {VERMELHO}  (Cócó!){AMARELO}
      \\  V  /
     /    \\ 
    /      \\ 
    ^^    ^^ {RESET}"""

ovo_art = f"""{NEGRITO}{AMARELO}
     .---.
    /     \\
   |       |
    \\     /
     '---'{RESET}"""

galinha_fugindo = f"""{AMARELO}
                \\  |  /
                 \\   /
          _______/   \\_______
         /                   \\
        |   {RESET}{NEGRITO}TCHAU!{RESET}{AMARELO}          |   {VERMELHO}   _  _  _ {AMARELO}
        |      /\\     /\\     |  {VERMELHO}  (_)(_)(_){AMARELO}
        |     /  \\   /  \\    |  {VERMELHO}   /  /  / {AMARELO}
         \\___/    \\_/    \\___/  
           !!      !!     !!  {RESET}
    {VERMELHO} (A galinha fugiu com o ovo!){RESET}
"""

ovo_quebrado = f"""{CINZA}
           _____
        .-'     '-.
       /   {AMARELO}_   _{RESET}{CINZA}   \\
      /   {AMARELO}(_) (_){RESET}{CINZA}   \\
     |     {AMARELO} / \\{RESET}{CINZA}      |
      \\    {VERMELHO}/\\ /\\{RESET}{CINZA}    /  {AMARELO}  .  '  . {RESET}
       {NEGRITO}'-./ v \\.-'{RESET} {AMARELO}  '  {AMARELO}Y{AMARELO}  ' {RESET}
     {AMARELO}    (_____)      .  '  . {RESET}
    {VERMELHO}   (O ovo quebrou!){RESET}
"""

comodos_arte = {
    "cozinha": f"{AZUL}╔════════ COZINHA ════════╗\n║  [ == ]          (  )   ║\n║  |    |  _______  ||    ║\n║  |____| |       | ||    ║\n║  [____] |_______|       ║\n╚═════════════════════════╝{RESET}",
    "sala": f"{MAGENTA}╔══════════ SALA ═════════╗\n║   _______     _______   ║\n║  |  _TV_ |   |       |  ║\n║  |_______|   | SOFÁ  |  ║\n║      ||      |_______|  ║\n╚═════════════════════════╝{RESET}",
    "quarto": f"{CIANO}╔═════════ QUARTO ════════╗\n║   __________     ____   ║\n║  |          |   |    |  ║\n║  |   CAMA   |   | ABJ|  ║\n║  |__________|   |____|  ║\n╚═════════════════════════╝{RESET}",
    "banheiro": f"{AZUL}╔════════ BANHEIRO ═══════╗\n║   _|_            ____   ║\n║  |   |   🚿     /    \\  ║\n║  |___|  VASO    |    |  ║\n║                 \\____/  ║\n╚═════════════════════════╝{RESET}",
    "varanda": f"{VERDE}╔════════ VARANDA ════════╗\n║   🌿  🌿  🌿     _|_    ║\n║   |¯¯¯¯¯¯¯|     |   |   ║\n║   | CADEIRA|    |___|   ║\n║   |_______|    PLANTAS  ║\n╚═════════════════════════╝{RESET}"
}

# ---------------- CONFIGURAÇÃO DO JOGO ----------------
comodos = list(comodos_arte.keys())
local_do_ovo = random.choice(comodos)
local_atual = "sala"
tentativas = 0
LIMITE_TENTATIVAS = 3

# ---------------- INÍCIO ----------------
tocar_musica_fundo()
print(f"\n{VERDE}{NEGRITO}==============================================")
print("     🐔 O MISTÉRIO DO OVO DA GALINHA 🐔")
print(f"=============================================={RESET}")
print(galinha_art)
if som_galinha: som_galinha.play()
time.sleep(1)

# ---------------- LOOP DO JOGO ----------------
while True:
    restantes = LIMITE_TENTATIVAS - tentativas
    
    print(f"\n{CINZA}─────────────────────────────────────────────{RESET}")
    cor_tentativa = VERDE if restantes > 1 else VERMELHO
    print(f"❤️ Vidas: {cor_tentativa}{restantes}{RESET}")
    print(f"📍 Você está na: {NEGRITO}{local_atual.upper()}{RESET}")
    print(comodos_arte[local_atual])

    print(f"\n{AMARELO}Para onde deseja ir?{RESET}")
    botoes = "  ".join([f"{CINZA}[{CIANO}{c}{CINZA}]{RESET}" for c in comodos])
    print(botoes)

    escolha = input(f"\n{NEGRITO}📝 Digite o cômodo: {RESET}").lower().strip()
    
    if escolha not in comodos:
        print(f"{VERMELHO}❌ Esse cômodo não existe!{RESET}")
        continue

    tentativas += 1
    local_atual = escolha
    
    # Efeitos de transição
    if som_passo: som_passo.play()
    time.sleep(0.5)
    if som_comodo: som_comodo.play()
    
    # 1. VERIFICAÇÃO DE VITÓRIA
    if local_atual == local_do_ovo:
        pygame.mixer.music.stop()
        if som_vitoria: som_vitoria.play()
        print(f"\n{VERDE}{NEGRITO}✨ INCRÍVEL! VOCÊ ACHOU O OVO NA {local_atual.upper()}! ✨{RESET}")
        print(ovo_art)
        print(f"{AMARELO}🏆 Você venceu com {tentativas} tentativas!{RESET}")
        time.sleep(5) 
        break
    
    # 2. VERIFICAÇÃO DE DERROTA (GAME OVER)
    elif tentativas >= LIMITE_TENTATIVAS:
        pygame.mixer.music.stop()
        if som_gameover: som_gameover.play()
        
        # Escolha aleatória da arte de derrota
        derrota_da_vez = random.choice([galinha_fugindo, ovo_quebrado])
        
        print(f"\n{VERMELHO}{NEGRITO}❌ GAME OVER! VOCÊ PERDEU!{RESET}")
        print(derrota_da_vez)
        print(f"{CINZA}O ovo estava na: {NEGRITO}{local_do_ovo.upper()}{RESET}")
        time.sleep(6)
        break
        
    else:
        print(f"{VERMELHO}🔎 Vazio... Cuidado, restam {LIMITE_TENTATIVAS - tentativas} tentativas!{RESET}")