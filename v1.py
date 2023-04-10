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

# Defina as propriedades do quadrado
square_size = 25
square_color = BLACK
square_position = [(WINDOW_WIDTH - square_size) / 3, (WINDOW_HEIGHT - square_size) / 2]

# Defina as propriedades do segundo quadrado quadrado
square_size2 = 25
square_color2 = RED
square_position2 = [(1066 - square_size2) , (WINDOW_HEIGHT - square_size2) / 2]
square_direction = 3

# Variáveis para controlar a mudança aleatória de direção
change_direction_start_time = time.time()
change_direction_duration = 1  # segundos

# Defina a velocidade de movimento do quadrado
movement_speed1 = 0.8
movement_speed2 = 1

# Defina a opção de tela cheia
fullscreen = False

# Variável para controlar o tempo de duração da velocidade aumentada
speed_up_duration = 1  # segundos

# Variável para armazenar o tempo em que a velocidade foi aumentada
speed_up_start_time = None

touch = 0

# Crie o loop principal do jogo
while True:
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
                movement_speed1 = 2
                speed_up_start_time = time.time()
                pygame.time.set_timer(pygame.USEREVENT, int(speed_up_duration * 1000)) # timer para voltar a velocidade normal depois de 2 segundos

        # Se o temporizador expirar, volte a velocidade do movimento do quadrado para 1.2
        elif event.type == pygame.USEREVENT:
            movement_speed1 = 1.2

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
    if square_direction == 1:
        square_position2[0] -= movement_speed2
        if square_position2[0] < -square_size:
            square_position2[0] = WINDOW_WIDTH
    if square_direction == 2:
        square_position2[0] += movement_speed2
        if square_position2[0] > WINDOW_WIDTH:
            square_position2[0] = -square_size
    if square_direction == 3:
        square_position2[1] -= movement_speed2
        if square_position2[1] < -square_size:
            square_position2[1] = WINDOW_HEIGHT
    if square_direction == 4:
        square_position2[1] += movement_speed2
        if square_position2[1] > WINDOW_HEIGHT:
            square_position2[1] = -square_size

    # Verifique se é hora de mudar aleatoriamente a direção do segundo quadrado
    if time.time() - change_direction_start_time > change_direction_duration:
        square_direction = sample([1, 2, 3, 4], 1)[0]
        change_direction_start_time = time.time()
    
    hitbox1 = pygame.Rect(square_position[0], square_position[1], 25, 25)
    hitbox2 = pygame.Rect(square_position2[0], square_position2[1], 25, 25)
    # Limpe a tela
    screen.fill(WHITE)

    # Desenhe o quadrado
    pygame.draw.rect(screen, square_color, (square_position[0], square_position[1], square_size, square_size))

    if hitbox1.colliderect(hitbox2):
        touch = True
    
    if touch == False:
        pygame.draw.rect(screen, square_color2, (square_position2[0], square_position2[1], square_size2, square_size2))

    # Atualize a janela
    pygame.display.update()