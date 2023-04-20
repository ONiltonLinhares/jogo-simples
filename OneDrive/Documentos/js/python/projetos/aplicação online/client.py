import pygame
from network import Network
from player import Player

width = 1300
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

# Definir as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Definindo a fonte do texto
pygame.font.init()
fonte_titulo = pygame.font.SysFont(None, 100)
fonte_instruções = pygame.font.SysFont(None, 30)

# Definindo o texto das instruções
instrucoes = ["- Use as setas do teclado para mover o quadrado preto",
              
              "- Pegue o quadrado vermelho",

              "- Aperte espaço para acelerar temporariamente",

              "- Aperte 'f' para entrar em tela cheia",

              "- Aperte enter para começar"
              ]

def redrawWindow(win,player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

n = Network()
p = n.getP()
pos = [p.x, p.y]
def main(win, p):

    tela1 = True

    while True:
        while tela1:
            # Verificando os eventos
            for evento in pygame.event.get():
                # Verificando se o jogador fechou a janela
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Pintando a janela de branco
            win.fill(WHITE)

            # Desenhando o título
            texto_pega1 = fonte_titulo.render("Pega-", True, BLACK)
            texto_pega2 = fonte_titulo.render("Pega", True, RED)
            texto_pega1_rect = texto_pega1.get_rect(midright=( width // 2 - 1, height // 4))
            texto_pega2_rect = texto_pega2.get_rect(midleft=(width // 2 + 1, height // 4))
            win.blit(texto_pega1, texto_pega1_rect)
            win.blit(texto_pega2, texto_pega2_rect)

            # Desenhando as instruções
            for i, instrucao in enumerate(instrucoes):
                texto = fonte_instruções.render(instrucao, True, BLACK)
                texto_rect = texto.get_rect(center=(width // 2, height // 2 + i * 30))
                win.blit(texto, texto_rect)

            # Atualizando a janela
            pygame.display.update()

            # analisando as interações do usuario 
            for event in pygame.event.get():
                # Se o usuário clicar no botão "X" da janela, saia do jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Se uma tecla for pressionada
                elif event.type == pygame.KEYDOWN:
                    # Adicione a opção de tela cheia
                    if event.key == pygame.K_f:
                        fullscreen = not fullscreen
                        if fullscreen:
                            win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                        else:
                            win = pygame.display.set_mode((width, height))
                    # passando para o jogo caso o jogador aperte no enter
                    elif event.key == pygame.K_RETURN:
                        tela1 = False
        clock = pygame.time.Clock()

        p.x = pos[0]
        p.y = pos[1]

        while not tela1:
            clock.tick(60)
            p2 = n.send(p)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    tela = False
                    pygame.quit()

            if p.toque(p2.hitbox):
                tela1 = True

            p.move()
            redrawWindow(win, p, p2)

main(win, p)