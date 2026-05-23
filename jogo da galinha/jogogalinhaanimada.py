import pygame
import random

# Inicialização
pygame.init()

# Configurações da Janela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("🐔 Jogo da Galinha Animada")
relogio = pygame.time.Clock()

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AMARELO = (255, 215, 0)
VERMELHO = (200, 0, 0)
VERDE = (34, 139, 34)

# Variáveis de Animação
galinha_x = 100
galinha_y = 450
velocidade_x = 3
pulando = False
altura_pulo = 0

def desenhar_galinha(x, y):
    # Corpo
    pygame.draw.ellipse(tela, AMARELO, (x, y, 60, 45))
    # Cabeça
    pygame.draw.circle(tela, AMARELO, (x + 50, y + 10), 15)
    # Crista
    pygame.draw.ellipse(tela, VERMELHO, (x + 45, y - 10, 10, 15))
    # Bico
    pygame.draw.polygon(tela, (255, 100, 0), [(x+65, y+10), (x+75, y+15), (x+65, y+20)])

# Loop do Jogo
rodando = True
while rodando:
    tela.fill((135, 206, 235)) # Fundo Azul Céu

    # 1. Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE: # Pula ao apertar Espaço
                pulando = True

    # 2. Lógica de Movimento
    galinha_x += velocidade_x
    if galinha_x > LARGURA:
        galinha_x = -80 # Reseta posição
    
    # Lógica de Pulo simples
    if pulando:
        altura_pulo -= 5
        if altura_pulo < -100:
            pulando = False
    elif altura_pulo < 0:
        altura_pulo += 5

    # 3. Desenhar Cenário
    pygame.draw.rect(tela, VERDE, (0, 500, LARGURA, 100)) # Gramado
    
    # Desenhar Galinha
    desenhar_galinha(galinha_x, galinha_y + altura_pulo)

    # Texto Instrução
    fonte = pygame.font.SysFont("Arial", 24)
    texto = fonte.render("Aperte ESPAÇO para pular!", True, PRETO)
    tela.blit(texto, (20, 20))

    pygame.display.flip()
    relogio.tick(60) # 60 FPS

pygame.quit()