import pygame
import time
from random import sample
from time import sleep

# inicialize o Pygame
pygame.init()

# Definir as dimensões da janela
WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 600

# Definir as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Crie a janela
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pega-Pega")
screen.fill(WHITE)  

# Defina a opção de tela cheia
fullscreen = False

# Definindo a fonte do texto
fonte_titulo = pygame.font.SysFont(None, 100)
fonte_instruções = pygame.font.SysFont(None, 30)

# Definindo o texto das instruções
instrucoes = ["- Use as setas do teclado para mover o quadrado preto",
              
              "- Pegue o quadrado vermelho",

              "- Aperte espaço para acelerar temporariamente",

              "- Aperte 'f' para entrar em tela cheia",

              "- Aperte enter para começar"
              ]

tela1 = True

#loop das telas

while True:

    # Loop da tela 1
    while tela1:
        # Verificando os eventos
        for evento in pygame.event.get():
            # Verificando se o jogador fechou a janela
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Pintando a janela de branco
        screen.fill(WHITE)

        # Desenhando o título
        texto_pega1 = fonte_titulo.render("Pega-", True, BLACK)
        texto_pega2 = fonte_titulo.render("Pega", True, RED)
        texto_pega1_rect = texto_pega1.get_rect(midright=(WINDOW_WIDTH // 2 - 1, WINDOW_HEIGHT // 4))
        texto_pega2_rect = texto_pega2.get_rect(midleft=(WINDOW_WIDTH // 2 + 1, WINDOW_HEIGHT // 4))
        screen.blit(texto_pega1, texto_pega1_rect)
        screen.blit(texto_pega2, texto_pega2_rect)

        # Desenhando as instruções
        for i, instrucao in enumerate(instrucoes):
            texto = fonte_instruções.render(instrucao, True, BLACK)
            texto_rect = texto.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + i * 30))
            screen.blit(texto, texto_rect)

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
                        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
                # passando para o jogo caso o jogador aperte no espaço
                elif event.key == pygame.K_RETURN:
                    tela1 = False
                
    # Defina as propriedades do quadrado
    square_size = 25
    square_color = BLACK
    square_position = [(WINDOW_WIDTH - square_size) / 3, (WINDOW_HEIGHT - square_size) / 2]

    # Defina as propriedades do segundo quadrado quadrado
    square_size2 = 25
    square_color2 = RED
    square_position2 = [(1066 - square_size2) , (WINDOW_HEIGHT - square_size2) / 2]
    square_direction = 0

    # Variáveis para controlar a mudança de direção
    change_direction_start_time = time.time()
    change_direction_duration = 0.5  # segundos


    # Defina a velocidade de movimento do quadrado
    movement_speed1 = 0.65
    movement_speed2 = 1

    # Variável para controlar o tempo de duração da velocidade aumentada
    speed_up_duration = 1  # segundos

    # Variável para armazenar o tempo em que a velocidade foi aumentada
    speed_up_start_time = None

    touch = 0

    # Crie o loop principal do jogo
    while not tela1:
        # Trate os eventos
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
                        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
                        
                # Se a tecla de espaço for pressionada, aumente a velocidade do movimento do quadrado
                elif event.key == pygame.K_SPACE:
                    movement_speed1 = 1.1
                    speed_up_start_time = time.time()
                    pygame.time.set_timer(pygame.USEREVENT, int(speed_up_duration * 1000)) # timer para voltar a velocidade normal depois de 2 segundos

            # Se o temporizador expirar, volte a velocidade do movimento do quadrado para 1.2
            elif event.type == pygame.USEREVENT:
                movement_speed1 = 0.65

        # Obtenha as teclas pressionadas
        keys = pygame.key.get_pressed()
        
        # Verifique se a tecla de seta correspondente está pressionada e mova o quadrado naquela direção
        speed_multiplier = 1  # multiplicador de velocidade padrão
        if keys[pygame.K_LEFT]:
            square_position[0] -= movement_speed1 * speed_multiplier
            if square_position[0] < -square_size:
                square_position[0] = WINDOW_WIDTH
        if keys[pygame.K_RIGHT]:
            square_position[0] += movement_speed1 * speed_multiplier
            if square_position[0] > WINDOW_WIDTH:
                square_position[0] = -square_size
        if keys[pygame.K_UP]:
            square_position[1] -= movement_speed1 * speed_multiplier
            if square_position[1] < -square_size:
                square_position[1] = WINDOW_HEIGHT
        if keys[pygame.K_DOWN]:
            square_position[1] += movement_speed1 * speed_multiplier
            if square_position[1] > WINDOW_HEIGHT:
                square_position[1] = -square_size
        
        # Mova o segundo quadrado

        hitbox1 = pygame.Rect(square_position[0], square_position[1], 25, 25)
        hitbox2 = pygame.Rect(square_position2[0], square_position2[1], 25, 25)
        hitbox3 = pygame.Rect(square_position2[0], square_position2[1], 50, 50)
        hitbox4 = pygame.Rect(square_position[0], square_position[1], 200, 200)

        if hitbox3.colliderect(hitbox4) or hitbox4.colliderect(hitbox3):
            if keys[pygame.K_LEFT] :
                square_direction = 1
            if keys[pygame.K_UP] :
                square_direction = 3
            if keys[pygame.K_RIGHT]:
                square_direction = 2
            if keys[pygame.K_DOWN]:
                square_direction = 4

            
        if square_direction == 1: # esquerda
            square_position2[0] -= movement_speed2
            if square_position2[0] < -square_size:
                square_position2[0] = WINDOW_WIDTH
        if square_direction == 2: # direita
            square_position2[0] += movement_speed2
            if square_position2[0] > WINDOW_WIDTH:
                square_position2[0] = -square_size
        if square_direction == 3: # cima
            square_position2[1] -= movement_speed2
            if square_position2[1] < -square_size:
                square_position2[1] = WINDOW_HEIGHT
        if square_direction == 4: # baixo
            square_position2[1] += movement_speed2
            if square_position2[1] > WINDOW_HEIGHT:
                square_position2[1] = -square_size

        # Verifique se é hora de mudar aleatoriamente a direção do segundo quadrado
        if time.time() - change_direction_start_time > change_direction_duration:
            square_direction = sample([1, 2, 3, 4], 1)[0]
            change_direction_start_time = time.time()

        # Limpe a tela
        screen.fill(WHITE)

        # Desenhe o quadrado
        pygame.draw.rect(screen, square_color, (square_position[0], square_position[1], square_size, square_size))

        if hitbox1.colliderect(hitbox2):
            tela1 = True

        pygame.draw.rect(screen, square_color2, (square_position2[0], square_position2[1], square_size2, square_size2))

        # Atualize a janela
        pygame.display.update()